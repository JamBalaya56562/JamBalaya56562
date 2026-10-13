"""Update dynamic profile README sections from public GitHub data.

Usage:
  python3 profile.py prs <readme>
      Rewrite the <!--START_SECTION:prs--> block with recent merged PRs
  python3 profile.py commit <repo> <branch> <head> <message> <files...>
      Print a createCommitOnBranch request body as JSON

Requires the GitHub CLI (`gh`) authenticated through GH_TOKEN.
"""

import base64
import json
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from html import escape
from urllib.parse import quote_plus

USER = os.environ.get("PROFILE_USER", "JamBalaya56562")
# Owners whose repositories are not counted as outside contributions.
HOME_OWNERS = {USER}
TOP_REPOS = 6
LATEST_PRS = 8


def gh(*args):
    out = subprocess.run(["gh", *args], check=True, capture_output=True, encoding="utf-8")
    return json.loads(out.stdout)


def search(query, per_page=100, page=1):
    return gh(
        "api", "-X", "GET", "search/issues",
        "-f", f"q=author:{USER} is:pr is:merged {query}",
        "-f", "sort=updated", "-f", "order=desc",
        "-f", f"per_page={per_page}", "-f", f"page={page}",
    )


def external_query():
    return " ".join(f"-user:{owner}" for owner in sorted(HOME_OWNERS))


def recent_prs(pages=3):
    """Newest merged PRs outside home owners (search returns 100 per page)."""
    prs = []
    for page in range(1, pages + 1):
        res = search(external_query(), page=page)
        for item in res["items"]:
            prs.append({
                "repo": item["repository_url"].split("/repos/", 1)[1],
                "title": item["title"],
                "url": item["html_url"],
                "closed": item["closed_at"][:10],
            })
        if len(res["items"]) < 100:
            break
    prs.sort(key=lambda p: p["closed"], reverse=True)
    return prs


def repo_info(repo):
    data = gh("api", f"repos/{repo}")
    return data["stargazers_count"], data["owner"]["avatar_url"]


def merged_count(repo):
    return search(f"repo:{repo}", per_page=1)["total_count"]


def title(text):
    """Escape a PR title for use as Markdown link text."""
    return re.sub(r"([\\\[\]])", r"\\\1", escape(text, quote=False))


def human(n):
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def replace_section(text, name, body):
    pattern = re.compile(
        rf"(<!--START_SECTION:{name}-->).*?(<!--END_SECTION:{name}-->)", re.S
    )
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(2)}", text)


def cmd_prs(readme):
    total = search(external_query(), per_page=1)["total_count"]
    prs = recent_prs()
    # Pick repositories active in the recent window, ranked by all-time count.
    active = [repo for repo, _ in Counter(p["repo"] for p in prs).most_common(TOP_REPOS)]
    counts = {repo: merged_count(repo) for repo in active}
    active.sort(key=counts.get, reverse=True)

    lines = [
        "| | Repository | ⭐ Stars | Merged PRs |",
        "| :-: | :-- | --: | --: |",
    ]
    for repo in active:
        star, avatar = repo_info(repo)
        link = (
            f"https://github.com/{repo}/pulls?q="
            + quote_plus(f"is:pr author:{USER} is:merged")
        )
        lines.append(
            f'| <img src="{avatar}&s=40" width="20" height="20" alt=""> '
            f"| [{repo}](https://github.com/{repo}) | {human(star)} "
            f"| [{counts[repo]:,}]({link}) |"
        )

    lines += ["", "**🆕 Latest merged pull requests**", ""]
    seen = set()
    latest = [p for p in prs if not (p["repo"] in seen or seen.add(p["repo"]))]
    for p in latest[:LATEST_PRS]:
        lines.append(
            f"- `{p['closed']}` **{p['repo']}** — [{title(p['title'])}]({p['url']})"
        )
    lines += [
        "",
        f"<sub>{total:,} merged PRs to other projects "
        f"· updated {datetime.now(timezone.utc):%Y-%m-%d} by GitHub Actions</sub>",
    ]

    with open(readme, encoding="utf-8") as f:
        text = f.read()
    with open(readme, "w", encoding="utf-8", newline="\n") as f:
        f.write(replace_section(text, "prs", "\n".join(lines)))


def cmd_commit(repo, branch, head, message, *files):
    gql = os.path.join(os.path.dirname(__file__), "..", "api", "createCommitOnBranch.gql")
    with open(gql, encoding="utf-8") as f:
        query = f.read()
    additions = []
    for path in files:
        with open(path, "rb") as f:
            additions.append({"path": path, "contents": base64.b64encode(f.read()).decode()})
    json.dump({
        "query": query,
        "variables": {
            "githubRepository": repo,
            "branchName": branch,
            "expectedHeadOid": head,
            "commitMessage": message,
            "files": additions,
        },
    }, sys.stdout)


if __name__ == "__main__":
    {"prs": cmd_prs, "commit": cmd_commit}[sys.argv[1]](*sys.argv[2:])
