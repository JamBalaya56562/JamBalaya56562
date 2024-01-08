# 🫶Contributing Guidelines

We would love for you to contribute and help make it even better than it is today!  
As a contributor, here are the guidelines we would like you to follow:

 - [🤝Code of Conduct](#code-of-conduct)
 - [🔎Question or Problem?](#question-or-problem)
 - [🐛Issues and Bugs](#issues-and-bugs)
 - [🚀Feature Requests](#feature-requests)
 - [🎫Submission Guidelines](#submission-guidelines)
 - [📃Commit Message Format](#commit-message-format)

## 🤝Code of Conduct

Help us keep JamBalaya56562 open and inclusive.  
Please read and follow our [Code of Conduct][coc].

## 🔎Question or Problem?

Do not open issues for general support questions as we want to keep GitHub issues for bug reports and feature requests.  
Instead, we recommend using [Stack Overflow][so] to ask support-related questions.

[Stack Overflow][so] is a much better place to ask questions since:

- there are thousands of people willing to help on [Stack Overflow][so]
- questions and answers stay available for public viewing so your question/answer might help someone else
- [Stack Overflow][so]'s voting system assures that the best answers are prominently visible.

To save your and our time, we will systematically close all issues that are requests for general support and redirect people to [Stack Overflow][so].  

## 🐛Issues and Bugs

If you find a bug in the source code, you can help us by [submitting an issue](#submitting-an-issue).  
Even better, you can [submit a Pull Request](#submitting-a-pull-request-pr) with a fix.

## 🚀Feature Requests

You can *request* a new feature by [submitting an issue](#submitting-an-issue).  
If you would like to *implement* a new feature, please consider the size of the change in order to determine the right steps to proceed:

* For a **Major Feature**, first open an issue and outline your proposal so that it can be discussed.  
  This process allows us to better coordinate our efforts, prevent duplication of work, and help you to craft the change so that it is successfully accepted into the project.

> [!NOTE]
> Adding a new topic to the documentation, or significantly re-writing a topic, counts as a major feature.

* **Small Features** can be crafted and directly [submitted as a Pull Request](#submitting-a-pull-request-pr).

## 🎫Submission Guidelines

### Submitting an Issue

Before you submit an issue, please search the issue tracker.  
An issue for your problem might already exist and the discussion might inform you of workarounds readily available.

We want to fix all the issues as soon as possible, but before fixing a bug, we need to reproduce and confirm it.  
In order to reproduce bugs, we require that you provide a minimal reproduction.  
Having a minimal reproducible scenario gives us a wealth of important information without going back and forth to you with additional questions.

A minimal reproduction allows us to quickly confirm a bug (or point out a coding problem) as well as confirm that we are fixing the right problem.

We require a minimal reproduction to save maintainers' time and ultimately be able to fix more bugs.  
Often, developers find coding problems themselves while preparing a minimal reproduction.  
We understand that sometimes it might be hard to extract essential bits of code from a larger codebase, but we really need to isolate the problem before we can fix it.

Unfortunately, we are not able to investigate / fix bugs without a minimal reproduction, so if we don't hear back from you, we are going to close an issue that doesn't have enough info to be reproduced.

You can use our [issue templates][issue-template] and filling out the issue template.

### Submitting a Pull Request (PR)

Here’s how we suggest you go about proposing a change to this project:

1. Search [Pull requests][JamBalaya56562-pr] for an open or closed PR that relates to your submission.  You don't want to duplicate existing efforts.

2. Be sure that an issue describes the problem you're fixing, or documents the design for the feature you'd like to add.

3. [Fork this project][fork] to your account.

4. [Create a branch][branch] for the change you intend to make.

5. Make your changes to your fork.

6. [Send a pull request][pr] from your fork’s branch to our `main` branch.

Using the web-based interface to make changes is fine too, and will help you
by automatically forking the project and prompting to send a pull request too.

## 📃Commit Message Format

*This specification is inspired by and supersedes the [AngularJS commit message format][commit-message-format].*

We have very precise rules over how our Git commit messages must be formatted.  
This format leads to **easier to read commit history**.

Each commit message consists of a **header**, a **body**, and a **footer**.

```
<header>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The `header` is mandatory and must conform to the [Commit Message Header](#commit-message-header) format.

The `body` is mandatory for all commits except for those of type "docs".  
When the body is present it must be at least 20 characters long and must conform to the [Commit Message Body](#commit-message-body) format.

The `footer` is optional.  
The [Commit Message Footer](#commit-message-footer) format describes what the footer is used for and the structure it must have.

### Commit Message Header

```
<type>(<scope>): <summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope: biome|bun|ci|common|css|docker|git|security|test|vscode ...
  │
  └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test
```

The `<type>` and `<summary>` fields are mandatory, the `(<scope>)` field is optional.

#### Type

Must be one of the following:

* **build**: Changes that affect the build system or external dependencies (example scopes: npm)
* **chore**: Updating grunt tasks etc, no production code change
* **ci**: Changes to our CI configuration files and scripts (examples: CircleCi, SauceLabs)
* **docs**: Documentation only changes
* **feat**: A new feature
* **fix**: A bug fix
* **perf**: A code change that improves performance
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **test**: Adding missing tests or correcting existing tests
* **upgrade**: Version up

##### Scope

The following is the example list of supported scopes:

* `biome`
* `bun`
* `common`
* `css`
* `docker`
* `git`
* `npm`
* `security`
* `test`
* `vscode`
* etc ...

##### Summary

Use the summary field to provide a succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize the first letter
* no dot (.) at the end
* to be easier to understand, recommend to add emoji♥️

### Commit Message Body

Just as in the summary, use the imperative, present tense: "fix" not "fixed" nor "fixes".

Explain the motivation for the change in the commit message body.  
This commit message should explain _why_ you are making the change.  
You can include a comparison of the previous behavior with the new behavior in order to illustrate the impact of the change.

### Commit Message Footer

The footer can contain information about breaking changes and deprecations and is also the place to reference GitHub issues, Jira tickets, and other PRs that this commit closes or is related to.
For example:

```
BREAKING CHANGE: <breaking change summary>
<BLANK LINE>
<breaking change description + migration instructions>
<BLANK LINE>
<BLANK LINE>
Fixes #<issue number>
```

or

```
DEPRECATED: <what is deprecated>
<BLANK LINE>
<deprecation description + recommended update path>
<BLANK LINE>
<BLANK LINE>
Closes #<pr number>
```

Breaking Change section should start with the phrase "BREAKING CHANGE: " followed by a summary of the breaking change, a blank line, and a detailed description of the breaking change that also includes migration instructions.

Similarly, a Deprecation section should start with "DEPRECATED: " followed by a short description of what is deprecated, a blank line, and a detailed description of the deprecation that also mentions the recommended update path.

[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[coc]: https://github.com/JamBalaya56562/JamBalaya56562/blob/main/CODE_OF_CONDUCT.md
[commit-message-format]: https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#
[JamBalaya56562-pr]: https://github.com/JamBalaya56562/JamBalaya56562/pulls
[fork]: https://help.github.com/articles/fork-a-repo/
[issue-template]: https://github.com/JamBalaya56562/JamBalaya56562/tree/main/.github/ISSUE_TEMPLATE
[pr]: https://help.github.com/articles/using-pull-requests/
[so]: https://stackoverflow.com
