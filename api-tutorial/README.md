# DraCor API Tutorial

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fapi-tutorial.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fapi-tutorial.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

This Jupyter notebook introduces the [DraCor API](https://dracor.org/doc/api) with Python. It shows how to send requests to the API with the library `requests`: information about the API, the list of corpora, the metadata of a corpus and the data of a single play, such as its characters and their spoken text. It gives examples of what can be done with the data, e.g. plots of the metadata with `pandas`, and counts of words in the spoken text of the characters with `nltk`, and it defines a generic function for requests to the API.

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). The tokenizer of `nltk` needs the data package `punkt_tab` (`nltk.download('punkt_tab')`, see the notebook). The server is set in the variable `API_URL` at the beginning of the notebook. The notebook asks for a corpus and a play while it runs; if no valid input is given, it uses the Swedish Drama Corpus (`swe`) and Strindberg's *Gillets hemlighet*.

## Version history

### Version 4: current DraCor API v1 (November 2026)

Ingo Börner updated the notebook to the current version of the DraCor API v1 ([#42](https://github.com/dracor-org/dracor-notebooks/issues/42)):

- The sex of the characters is read from the field `sex`, which replaced `gender` (`gender` is now a separate, optional field). Before, the examples on the sex of the characters failed with a `KeyError`.
- The metadata of a corpus come from the endpoint `/corpora/{corpusname}/metadata/csv`.
- The text and the comments use the URLs of API v1 (`/api/v1/…`, `/plays/`). The generic function `get()` uses `API_URL` as its default server.
- The comment on the data of `nltk` names `punkt_tab`, which newer versions of `nltk` need instead of `punkt`.
- The notebook has a metadata block, and the folder a `requirements.in` and a lock file.

Tested on 2026-11-17 with DraCor API 1.4.1 (production) and 1.5.0-rc.1 (staging), Python 3.10 and 3.12: all 38 code cells run.

Prepared with Claude Code (Anthropic) and reviewed by the authors.

Tag: will be set with the release.

### Version 3: DraCor API v1 (May 2024)

Henny Sluyter-Gäthje adapted the notebook to version 1 of the DraCor API (`https://dracor.org/api/v1/`, commit `db54c6c`, 2024-05-27): the endpoints `/plays/` and `characters` replaced `/play/` and `cast`. For the Jupyter Book, the input loops were limited and given default values (commits `48c8f53` and `7b28fdd`, 2024-05-31).

Tag: [`2026-11-15-baseline`](https://github.com/dracor-org/dracor-notebooks/tree/2026-11-15-baseline/api-tutorial), archived on Zenodo: [10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155).

### Version 2: workshop version (July 2022)

Henny Sluyter-Gäthje revised the tutorial for a workshop (`api-tutorial-dh.ipynb`, commit `3eba994`, 2022-07-15) and added comments, explanations and links to the documentation of the endpoints and libraries ([#9](https://github.com/dracor-org/dracor-notebooks/issues/9)–[#13](https://github.com/dracor-org/dracor-notebooks/issues/13)). This version, together with the generic function and the example by Ingo Börner, became `api-tutorial.ipynb` (commit `5fa63e2`, 2022-07-22). Heinz-Alexander Fütterer corrected typos (commit `2452d3f`, 2023-12-12).

Tag: none. The last state of this version is commit [`2452d3f`](https://github.com/dracor-org/dracor-notebooks/tree/2452d3f/api-tutorial) (2023-12-12). It uses the unversioned API (`https://dracor.org/api/`, now the legacy API v0).

### Version 1: first notebook (2019–2022)

Ingo Börner wrote the first notebook to demonstrate the basic functions of the DraCor API (commit `2448a7f`, 2019-09-05). In November 2021, he added the generic function for requests to the API, and in March 2022 the example that counts the characters of a corpus by sex (then `gender`).
