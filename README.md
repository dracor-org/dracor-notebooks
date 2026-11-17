# DraCor Notebooks

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24237154.svg)](https://doi.org/10.5281/zenodo.24237154) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dracor-org/dracor-notebooks/main)

A collection of notebooks to showcase the work with data extracted from [DraCor corpora](https://dracor.org) and in particular the [DraCor API](https://dracor.org/doc/api):

* [API Tutorial](https://github.com/dracor-org/dracor-notebooks/tree/main/api-tutorial) *(Henny Sluyter-Gäthje, Ingo Börner)*
* [DraCor-Based Reconstruction of Our Paper "To Catch a Protagonist"](https://github.com/dracor-org/dracor-notebooks/tree/main/catch-a-protagonist-in-dracor) *(Ingo Börner)*
* [Stylometric Text Classification](https://github.com/dracor-org/dracor-notebooks/tree/main/stylometric-text-classification) *(Robert Jäschke)*
* [Genre Analysis with DraCor](https://github.com/dracor-org/dracor-notebooks/tree/main/genre-analysis) *(Henny Sluyter-Gäthje)*
* [Contrastive Text Analysis](https://github.com/dracor-org/dracor-notebooks/tree/main/contrastive-text-analysis) *(Robert Jäschke)*
* [Gender Representation in German Plays](https://github.com/dracor-org/dracor-notebooks/tree/main/gender-visualization) *(Sandra Densch-Glazov, Leonie Wichers, Kyung Yun Choi, Benedikt Schuh)*
* [NLP-based Speech Analysis of DraCor Data](https://github.com/dracor-org/dracor-notebooks/tree/main/speech_analysis) *(Henny Sluyter-Gäthje)*

## Maintainers and contributing

The DraCor Notebooks are maintained by Ingo Börner, Henny Sluyter-Gäthje and Frank Fischer, with the support of Carsten Milling (technical lead of DraCor). Ideas for new notebooks, corrections and questions are welcome: please open an [issue](https://github.com/dracor-org/dracor-notebooks/issues) or write to info@dracor.org. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute, and [Get in Touch](https://dracor.org/doc/get-in-touch) on dracor.org for other ways to reach the DraCor community.

**Use of AI:** We use AI, namely Claude Code (Anthropic), to test, maintain and update the notebooks. All changes are reviewed by a maintainer.

## Binder
Notebooks can be executed locally or via Binder:
https://mybinder.org/v2/gh/dracor-org/dracor-notebooks/main

## Status and tested environments

The notebooks were last tested on 2026-11-15 against DraCor API v1 1.4.1, the legacy API v0 0.91.3 and staging 1.5.0-rc.1. Not all of them run with current package versions: some need PyDraCor 2.0.0, some still use the legacy API v0, which will be shut down. [TESTED-ENVIRONMENTS.md](TESTED-ENVIRONMENTS.md) lists, for each notebook, the API version, the server, the PyDraCor and Python versions and the test result. The exact package sets are in [environments/](environments/).

## How to cite

Please cite this repository using the metadata in [CITATION.cff](CITATION.cff). On GitHub, the "Cite this repository" button in the sidebar provides it as APA or BibTeX.

The notebooks are archived on Zenodo:

- All versions (resolves to the latest): [10.5281/zenodo.24237154](https://doi.org/10.5281/zenodo.24237154)
- Baseline as tested on 2026-11-15 (tag `2026-11-15-baseline`): [10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155)
