# NLP-based Speech Analysis of DraCor Data

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fspeech_analysis.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fspeech_analysis.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

This Jupyter notebook retrieves the spoken text of the characters of a play from the [DraCor API](https://dracor.org/doc/api) (version 1), annotates it with [spaCy](https://spacy.io) (sentences, tokens, lemmas, parts of speech, dependencies) and compares the speech of male and female characters: content words, words used only by male or only by female characters (with word clouds), the greatest differences in frequency, and adjective-noun pairs. The last section extends the retrieval and annotation to a whole corpus.

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). This includes the German language model `de_core_news_sm` of spaCy; for corpora in other languages, choose another [spaCy model](https://spacy.io/usage/models) in section 2.0 of the notebook. The server is set in the variable `base_url` in section 1.1. The notebook asks for a corpus and a play while it runs; if no valid input is given, it uses GerDraCor (`ger`) and Goethe's *Faust. In ursprünglicher Gestalt*.

Section 4 downloads the spoken text of all plays of the selected corpus, which takes a while for large corpora.

## Version history

### Version 2: sex of the characters, corpus section (August 2025)

Henny Sluyter-Gäthje adapted the notebook to DraCor API 1.1, which returns the sex of the characters in the field `sex` (before: `gender`), and added section 4, which extends the retrieval and annotation to a whole corpus (commit `542f216`, 2025-08-29).

Tested on 2026-11-15 with DraCor API 1.4.1 (production) and on 2026-11-17 with 1.5.0-rc.1 (staging), Python 3.11: the notebook runs without changes. In November 2026, a metadata block, this README and a `requirements.in` with a lock file were added (prepared with Claude Code (Anthropic) on behalf of the DraCor maintainers and reviewed by the author).

Tag: [`2026-11-15-baseline`](https://github.com/dracor-org/dracor-notebooks/tree/2026-11-15-baseline/speech_analysis), archived on Zenodo: [10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155).

### Version 1: first version (June 2024)

The first version by Henny Sluyter-Gäthje (commit `0e9c7ed`, 2024-06-12) uses version 1 of the DraCor API and compares the speech of the characters by gender (field `gender` at that time).

Tag: none. The last state of this version is commit [`0e9c7ed`](https://github.com/dracor-org/dracor-notebooks/tree/0e9c7ed/speech_analysis).
