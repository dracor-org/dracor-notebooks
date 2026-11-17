# Batch Download of DraCor Data with a Provenance Record

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fbatch_download.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fbatch_download.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

This Jupyter notebook downloads data of many plays at once, for a whole corpus or a selection of plays. It offers the same data as the Downloads tab on the page of a play on [dracor.org](https://dracor.org): networks as CSV, GEXF or GraphML, lists of characters, spoken text (optionally filtered, e.g. by the characters' sex), stage directions, and the full text as TEI. The files are named like the downloads on dracor.org.

Along with the data, the notebook writes a provenance record (`provenance.json`). Its core is the DraCor ID of each play and the commit (Git SHA) of the corpus version. With these, the download can be reproduced and cited. The notebook explains why this matters for living corpora such as DraCor, following CLS INFRA D7.3 *On Versioning Living and Programmable Corpora* ([10.5281/zenodo.11081934](https://doi.org/10.5281/zenodo.11081934)).

The idea goes back to [#2](https://github.com/dracor-org/dracor-notebooks/issues/2) by Frank Fischer.

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). The server is set in the variable `api_base` at the beginning of the notebook. The downloaded files are written to the folder `downloads/`, which is not part of the repository.

The notebook can also be turned into a command-line script with `jupyter nbconvert --to script` (see the section "Using the notebook as a script" in the notebook), e.g.:

```sh
python batch_download.py ger network.gexf --plays lessing-emilia-galotti --output downloads/ger-networks
```

## Version history

### Version 1: DraCor API v1, PyDraCor 3 (November 2026)

First version, based on PyDraCor 3.0 and DraCor API v1. Drafted with Claude Code (Anthropic) and reviewed by the author.

Tag: will be set with the release.
