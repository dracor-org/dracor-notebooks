# DraCor: Analysis of Network Values by Genre

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fgenre-analysis.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fgenre-analysis.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

This Jupyter notebook analyses the metadata of the plays in [DraCor](https://dracor.org/) with a focus on their genre. It reproduces the analysis in the blog post "[Comedy vs. Tragedy: Network Values by Genre](https://dlina.github.io/Network-Values-by-Genre/)" (Trilcke et al. 2015) with data from the [DraCor API](https://dracor.org/doc/api).

The analyses can be done for any DraCor corpus with genre information, and they can be parameterised, e.g.:
* filter the plays to be analysed by the number of acts or by the number of characters;
* select the network values to be investigated, e.g. *degree* or *size*;
* split the corpus into time intervals to analyse the development of the selected network values by genre.

Have fun experimenting!

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). The server is set in the variable `api_base` in section 1 of the notebook. The notebook asks for the corpus, the filters and the time intervals while it runs.

## Bibliography

Trilcke, Peer, Frank Fischer, Mathias Göbel, and Dario Kampkaspar. "Comedy vs. Tragedy: Network Values by Genre". *DLINA. Digital Literary Network Analysis*, 31 July 2015. https://dlina.github.io/Network-Values-by-Genre/.

## Version history

### Version 2: DraCor API v1 (November 2026)

Ingo Börner updated the notebook to version 1 of the DraCor API (`https://dracor.org/api/v1/`) before the shutdown of the legacy API v0 ([#37](https://github.com/dracor-org/dracor-notebooks/issues/37)):

- The server is set in the variable `api_base`; the metadata of a corpus come from the endpoint `/corpora/{corpusname}/metadata/csv`, which replaced `/corpora/{corpusname}/metadata` with the `Accept` header `text/csv`.
- The text notes that genre information is now available for more corpora.
- A duplicated cell (plots of the mean values) was removed.
- The notebook has a metadata block, and the folder a `requirements.in` and a lock file.

Tested on 2026-11-17 with DraCor API 1.4.1 (production) and 1.5.0-rc.1 (staging), Python 3.10 and 3.12. The results differ from those of version 1, because API v0 serves an older state of the corpora (GerDraCor: 734 plays under API v0, 788 under API v1).

Prepared with Claude Code (Anthropic) and reviewed by the author.

Tag: will be set with the release.

### Version 1: unversioned DraCor API (December 2021)

The first version of this notebook, by Henny Sluyter-Gäthje (commit `b29099f`, 2021-12-09), reproduces the analysis of Trilcke et al. (2015) with data from the DraCor API, which was not versioned at that time (`https://dracor.org/api/`, now the legacy API v0). In August 2025 (commit `8486121`), she fixed warnings of pandas in the plots and groupings.

Tag: [`2026-11-15-baseline`](https://github.com/dracor-org/dracor-notebooks/tree/2026-11-15-baseline/genre-analysis), archived on Zenodo: [10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155). This version runs only as long as the unversioned API is redirected to API v0 (0.91.3).
