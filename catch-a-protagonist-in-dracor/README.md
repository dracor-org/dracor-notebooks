# To catch a protagonist in DraCor

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fcatch-a-protagonist-in-dracor.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fcatch-a-protagonist-in-dracor.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

In the paper [*To Catch a Protagonist: Quantitative Dominance Relations in German-Language Drama (1730–1930)*](https://dh-abstracts.library.cmu.edu/works/6281) (Fischer, Trilcke et al. 2018) an algorithm is described, that allows to identify characters that are the quantitatively dominant characters of a play based on a set of network-based and count based measures:

> In order to systematically describe the extent of this deviation, we calculate eight values for each character of the 465 dramas of our corpus, three count-based measures (number of scenes a character appears in, number of speech acts, number of spoken words) and five network-related measures (degree, weighted degree, betweenness centrality, closeness centrality, eigenvector centrality). For each measurement a ranking is created. The rankings are then merged into two meta-rankings: one count-based and one network-based. The two meta-rankings are then combined into an overall ranking.

The original algorithm was implemented in the tool [Dramavis](https://github.com/lehkost/dramavis) by [Christopher Kittel](https://github.com/chreman). 

The following notebook adapts the code of the respective modules to work with data returned by the [DraCor API](https://dracor.org/doc/api). The aim is to be able to recreate the `*_chars.csv`-files that were used in the study.

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). The server is set in the variable `api_base` at the beginning of the notebook.

## Bibliography
Fischer, Frank, Peer Trilcke et al. „To Catch a Protagonist: Quantitative Dominance Relations in German-Language Drama (1730–1930)“. DH2018: »Puentes/Bridges«. 26–29 June 2018. Book of Abstracts / Libro de resúmenes, Red de Humanidades Digitales A. C., 2018, https://dh2018.adho.org/to-catch-a-protagonist-quantitative-dominance-relations-in-german-language-drama-1730-1930/.

## Version history

### Version 2: DraCor API v1 (August 2025)

Henny Sluyter-Gäthje updated the notebook to version 1 of the DraCor API (`https://dracor.org/api/v1/`, commit `f67867a`, 2025-08-29):

- The character data come from the endpoint `/corpora/{corpusname}/plays/{playname}/characters`, which replaced `/corpora/{corpusname}/play/{playname}/cast`.
- The characters' sex is in the field `sex`, which replaced `gender`.
- The data frame is created directly from the API response.

Tested on 2026-11-16 with DraCor API 1.4.1 (production) and 1.5.0-rc.1 (staging): the code runs unchanged and the results are identical. The text of the notebook was corrected for the endpoints of API v1, and the notebook now has a list of references.

Tag: [`2026-11-15-baseline`](https://github.com/dracor-org/dracor-notebooks/tree/2026-11-15-baseline/catch-a-protagonist-in-dracor), archived on Zenodo: [10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155). It holds the code of this version, before the corrections of the text.

### Version 1: unversioned DraCor API (November 2021)

The first version of this notebook, by Ingo Börner, reconstructs the algorithm of the paper "To Catch a Protagonist" (Fischer, Trilcke et al. 2018) with data from the DraCor API, which was not versioned at that time (`https://dracor.org/api/`, now the legacy API v0). The notebook was prepared alongside the reimplementation of the original algorithm for the talk "To Catch a Protagonist … Once Again. An Attempt to Recreate a Corpus-Based Study Using Linked Data" by Ingo Börner, Peer Trilcke, Frank Fischer, Carsten Milling and Henny Sluyter-Gäthje at the closing conference of the COST Action CA16204 "Distant Reading for European Literary History", held online together with CLS INFRA and organised by the Jagiellonian University, Kraków (22 April 2022; see the [conference programme](https://www.distant-reading.net/events/conference-programme/), Session 5a).

Heinz-Alexander Fütterer (2023, commit `2452d3f`) and Luca Giovannini (2024, commit `da07079`) corrected typos in the text.

Tag: none. The last state of this version is commit [`da07079`](https://github.com/dracor-org/dracor-notebooks/tree/da07079/catch-a-protagonist-in-dracor) (2024-06-05).
