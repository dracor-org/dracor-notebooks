# Text Classification with DraCor

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fstylometric-text-classification.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fstylometric-text-classification.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

This Jupyter notebook demonstrates the use of the [DraCor API](https://dracor.org/doc/api) for machine learning. It tests to what extent the author of a play can be identified from its text alone, a typical application of [stylometry](https://en.wikipedia.org/wiki/Stylometry). It downloads the spoken text of all plays of the German Drama Corpus (GerDraCor) that have a single author, and trains and evaluates a Naive Bayes classifier ([scikit-learn](https://scikit-learn.org)) with different representations of the texts: frequencies of words and word bigrams, TF-IDF, and frequencies of characters and character bigrams.

The notebook was written by Robert Jäschke (original file [here](https://scm.cms.hu-berlin.de/ibi/notebooks/-/blob/master/DraCor.ipynb)).

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). The server is set in the variable `dracor_api` at the beginning of the notebook.

**Running time:** about 15–20 minutes on a current laptop (tested on an Apple Silicon Mac in November 2026). Downloading the spoken text of the 774 plays takes about 4 minutes; the classification with rare word bigrams (section "Rare Bigrams") takes about 10 minutes, the other experiments between a few seconds and about a minute each.

## Version history

### Version 3: DraCor API v1 (November 2026)

Ingo Börner updated the notebook to version 1 of the DraCor API before the shutdown of the legacy API v0 ([#38](https://github.com/dracor-org/dracor-notebooks/issues/38)):

- The notebook uses `https://dracor.org/api/v1` (variable `dracor_api`) and the endpoint `/corpora/{corpusname}/plays/{playname}/spoken-text`, which replaced `/play/`. The plays of a corpus are listed under `plays`, which replaced `dramas`.
- The data are downloaded with the library `requests` instead of `urllib`: dracor.org returns large responses of API v1 compressed (gzip), which `urllib` does not decompress.
- Two typos in the text were corrected.
- The notebook has a metadata block, and the folder a `requirements.in` and a lock file.

The results differ from those of version 2, because API v0 serves an older state of GerDraCor (734 plays, 720 of them by a single author, under API v0; 788 and 774 under API v1). The scores also vary between runs, because the split into training and test data is random.

Tested on 2026-11-17 with DraCor API 1.4.1 (production) and 1.5.0-rc.1 (staging), Python 3.12; the complete run took 20 and 13 minutes.

Prepared with Claude Code (Anthropic) and reviewed by the author.

Tag: will be set with the release.

### Version 2: English version (March 2022)

Robert Jäschke translated the notebook into English (commit `aa03328`, 2022-03-31). It uses the DraCor API, which was not versioned at that time (`https://dracor.org/api/`, now the legacy API v0).

Tag: [`2026-11-15-baseline`](https://github.com/dracor-org/dracor-notebooks/tree/2026-11-15-baseline/stylometric-text-classification), archived on Zenodo: [10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155). This version runs only as long as the unversioned API is redirected to API v0 (0.91.3).

### Version 1: German version (November 2021)

The first version of the notebook, "Textklassifikation mit DraCor", in German, by Robert Jäschke. Frank Fischer added it to the DraCor Notebooks (commit `9c23da7`, 2021-11-19).

Tag: none. The last state of this version is commit [`9c23da7`](https://github.com/dracor-org/dracor-notebooks/tree/9c23da7/stylometric-text-classification).
