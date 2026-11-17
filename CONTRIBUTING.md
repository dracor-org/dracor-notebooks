# Contributing to the DraCor Notebooks

Thank you for your interest in the DraCor Notebooks. The notebooks show how to do research with the drama corpora of [DraCor](https://dracor.org) and the DraCor API, and we welcome ideas, corrections and new notebooks.

## Maintainers

The DraCor Notebooks are maintained by Ingo Börner, Henny Sluyter-Gäthje and Frank Fischer, with the support of Carsten Milling (technical lead of DraCor). The authors of each notebook are named at its beginning and in the `CITATION.cff` of the repository.

## Ideas, questions and problems

- **Open an issue** in this repository, for example if a notebook no longer runs, if you find an error, or if you have an idea for a new notebook.
- **Write to info@dracor.org** if you prefer not to use GitHub.
- For other ways to get in touch with the DraCor community, see [Get in Touch](https://dracor.org/doc/get-in-touch) on dracor.org.

Please open an issue **before** you start on a new notebook or a larger change, so that we can discuss it first. What we expect of contributions is still being discussed among the maintainers, so the guidelines below may change.

## Structure of a notebook folder

Each notebook has its own folder with:

| File | Content |
|---|---|
| `<name>.ipynb` | The notebook. It starts with a metadata block (authors, version, "Tested with") and ends with its references and its version history. |
| `README.md` | What the notebook does, how to run it, image credits, and the **version history**. |
| `requirements.in` | The packages the notebook needs. |
| `requirements.txt` | The locked versions, created with `uv pip compile --universal --python-version 3.10 requirements.in -o requirements.txt`. |
| `images/` | Images used in the notebook, credited in the README. |

The DraCor server is set in one variable, `api_base`, at the beginning of the notebook.

## Editing workflow

1. **Issue.** Describe the change in an issue, or refer to an existing one. For a new notebook, the maintainers create a label `nb: <folder>`.
2. **Branch.** Work on a branch named after the notebook folder, e.g. `dts-1.0` or `catch-a-protagonist`.
3. **Change in place.** Correct the notebook directly, code and text. Do not add "updated" notes to the notebook; the git history shows the changes. The notebook only states which API version it targets.
4. **Run the whole notebook** from top to bottom against the server it targets: production, or staging for a coming API release. Save it with its outputs. Check that the outputs contain no local paths, tokens or other personal data.
5. **Update the metadata.**
   - "Tested with" at the beginning of the notebook: API version, server, Python version, date.
   - Contributors: name everyone who changed the notebook, with their contribution.
   - Version history in the README: describe the changes. A **new version** starts when the code changes for a new version of the DraCor API, of a specification such as DTS, or of a package such as PyDraCor. Corrections of the text or of errors are part of the current version.
   - If dependencies changed: `requirements.in` and the lock file.
   - If AI tools were used for the notebook: a short note "Use of AI" at its end.
   - For a new notebook: add it to the table of contents of the book (`_toc.yml`).
6. **Pull request** to `main`. Say how you tested the notebook, and declare the use of AI tools (see below).
7. **Review.** At least one maintainer reviews the pull request before it is merged.
8. **Release.** The maintainers tag releases (e.g. `2026-11-15-baseline`) and archive them on Zenodo. The tag is then entered in the version history of each notebook it concerns.

## Use of AI

The maintainers use AI, namely Claude Code (Anthropic), to test, maintain and update the notebooks. All changes are reviewed by a maintainer before they are merged. Commits made with Claude Code are marked with a `Co-Authored-By: Claude` line.

If you use AI tools for a contribution, please say so in your pull request.

## Code of conduct

All contributors are expected to interact respectfully and constructively, and to help keep the DraCor community welcoming and inclusive.
