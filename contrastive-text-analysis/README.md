# Contrastive Text Analysis with DraCor and Scattertext

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fcontrastive-text-analysis.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fcontrastive-text-analysis.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

This Jupyter notebook uses [Scattertext](https://github.com/JasonKessler/scattertext) to visualise the linguistic differences between two groups of texts. It contrasts the spoken text of the male and female characters of Goethe's *Faust* ([GerDraCor](https://dracor.org/ger/goethe-faust-eine-tragoedie)), based on the sex of the characters as encoded in DraCor. The texts are retrieved with [PyDraCor](https://pypi.org/project/pydracor/) and processed with the German language model of [spaCy](https://spacy.io).

The result is an interactive HTML page: [goethe-faust-eine-tragoedie.html](goethe-faust-eine-tragoedie.html) (to view it, download the file and open it in a web browser).

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). This includes the German language model `de_dep_news_trf` of spaCy, which is based on a transformer model and installs PyTorch, so the installation is large. The server is set in the variable `api_base` in the section "Acquiring the Corpus". The notebook writes the HTML page to the folder of the notebook.

## Version history

### Version 3: PyDraCor 3, current DraCor API v1 (November 2026)

Ingo Börner updated the notebook to PyDraCor 3 and the current version of the DraCor API v1 ([#39](https://github.com/dracor-org/dracor-notebooks/issues/39)):

- PyDraCor 3 has a new interface: the play is retrieved with `DraCorAPI(host=api_base).get_play(corpus_name=…, play_name=…)` and its spoken text with `get_spoken_text_by_character()`, which returns objects instead of dictionaries.
- The sex of the characters is read from the field `sex`. With DraCor API 1.1.0 (July 2025), the former property `gender` was renamed to `sex`, and a new, optional `gender` was added for the TEI attribute `@gender` ([dracor-api#319](https://github.com/dracor-org/dracor-api/pull/319), [dracor-schema#94](https://github.com/dracor-org/dracor-schema/pull/94)). The column of the table is now called *Sex*.
- The installation commands are commented out; the packages are listed in `requirements.in` and the lock file, together with `six`, which `scattertext` imports without declaring it as a dependency.
- The example output `goethe-faust-eine-tragoedie.html` was created anew.
- The notebook has a metadata block, and the folder this README.

Tested on 2026-11-17 with DraCor API 1.4.1 (production) and 1.5.0-rc.1 (staging), PyDraCor 3.0.2, Python 3.11: 60 male and 18 female speakers; the speakers whose sex is unknown (37) are removed.

Prepared with Claude Code (Anthropic) and reviewed by the author.

Tag: will be set with the release.

### Version 2: PyDraCor 2 (January 2024)

Robert Jäschke switched the notebook to [PyDraCor](https://pypi.org/project/pydracor/) 2.0.0, which uses DraCor API v1 (commit `1af19e3`, 2024-01-09). It stopped working with DraCor API 1.1.0 (July 2025, `gender` renamed to `sex`) and with PyDraCor 3 (September 2025, new interface), because the installation of PyDraCor was not pinned.

Tag: [`2026-11-15-baseline`](https://github.com/dracor-org/dracor-notebooks/tree/2026-11-15-baseline/contrastive-text-analysis), archived on Zenodo: [10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155).

### Version 1: unversioned DraCor API (March 2022)

The first version by Robert Jäschke (`dracor-scattertext.ipynb`, commit `e48f4ad`, 2022-03-22) downloaded the spoken text by character as CSV from the DraCor API, which was not versioned at that time (`https://dracor.org/api/`, now the legacy API v0). It was moved into the folder `contrastive-text-analysis` (commit `0afbbc9`) and the example output was added (commit `f56f628`, 2022-03-25).

Tag: none. The last state of this version is commit [`f56f628`](https://github.com/dracor-org/dracor-notebooks/tree/f56f628/contrastive-text-analysis) (2022-03-25).
