# Analysis of Network Values by Genre

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fgenre-analysis.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fgenre-analysis.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

The jupyter notebook `Dracor_Genre_Analysis.ipynb` makes it possible to analyse the metadata of plays provided in [DraCor](https://dracor.org/) with the focus on the genre information provided for the plays. With the notebook you can perform analyses like the ones presented in "[Comedy vs. Tragedy: Network Values by Genre](https://dlina.github.io/Network-Values-by-Genre/)".   
You can perform the analyses on any DraCor corpus that is shipped with genre information and you are able to parameterize your analyses, e.g.
* filter which plays to want to analyse by the number of acts or by the number of characters
* set specific network values like *degree* or *size* that you want to investigate
* split the corpus into time frames to analyse the development of the selected network values by genre

Have fun experimenting! 

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). The server is set in the variable `api_base` in section 1 of the notebook. The notebook asks for the corpus, filters and time intervals while it runs.

## Version history

### Version 2: DraCor API v1 (November 2026)

Update to DraCor API v1, before the shutdown of the legacy API v0 ([#37](https://github.com/dracor-org/dracor-notebooks/issues/37)):
- The notebook uses `https://dracor.org/api/v1` (variable `api_base`) and the endpoint `/corpora/{corpusname}/metadata/csv`.
- Note on the corpora that now have genre information.
- A duplicated cell (mean values) is removed.
- Metadata block, `requirements.in` and lock file, `CITATION.cff`.

The results differ from those of version 1, because the corpora have grown since then; e.g. GerDraCor had 734 plays under API v0 and has 788 under API v1 (November 2026).

Prepared with Claude Code (Anthropic) on behalf of the DraCor maintainers and reviewed by the author.

Tag: will be set with the release.

### Version 1: unversioned DraCor API (December 2021)

First version by Henny Sluyter-Gäthje, a reproduction of the analysis "[Comedy vs. Tragedy: Network Values by Genre](https://dlina.github.io/Network-Values-by-Genre/)" with the DraCor API (commit b29099f, 9 December 2021). Fixes for warnings of pandas in August 2025 (8486121).

Last state: tag [`2026-11-15-baseline`](https://github.com/dracor-org/dracor-notebooks/tree/2026-11-15-baseline/genre-analysis) ([10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155)). It runs only through the redirect of the unversioned API to API v0 (0.91.3), which will be shut down.
