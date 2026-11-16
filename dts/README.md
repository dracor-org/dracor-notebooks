# DTS (Distributed Text Services) in DraCor

This Jupyter notebook introduces the implementation of the DTS (Distributed Text Services) API in DraCor. It demonstrates the endpoints Collection, Navigation and Document with examples and compares the DTS API with the regular DraCor API.

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). The server is set in the variable `api_base` at the beginning of the notebook.

## Image credits

| File | Description | Source | Licence |
|---|---|---|---|
| `images/dts-endpoint-overview.png` | Schema of the resource model underlying each DTS endpoint, the type of data it exposes and the required format of expression | Adapted by Ingo Börner from Almas, Bridget, Hugh Cayless, Thibault Clérice, Vincent Jolivet, Pietro Maria Liuzzo, Jonathan Robie, Matteo Romanello, and Ian Scott. "Distributed Text Services (DTS): A Community-Built API to Publish and Consume Text Collections as Linked Data." *Journal of the Text Encoding Initiative* (2023), Fig. 2. https://doi.org/10.4000/jtei.4352. First published in CLS INFRA D7.4 (2025), Fig. 12. | The original article is published under CC BY 4.0; the journal does not state a separate licence for its figures. |

Images keep the licence of their source; the licence of this repository does not apply to them.

## Versions

### Version 2: DTS 1.0 (November 2026)

The notebook was updated to version 1.0 of the DTS specification, which is implemented in DraCor API 1.5. Until API 1.5 is released on the production server, the notebook uses the staging server (`https://staging.dracor.org/api/v1/`).

Main changes compared to version 1:

- The Dublin Core metadata (`title`, `creator`, `language`) are returned as lists, titles as language-tagged values (`{"lang": "de", "value": "…"}`).
- The JSON-LD context is `https://dtsapi.org/context/v1.0.json`, which defines the terms in a DTS ontology instead of reusing the Hydra vocabulary.
- `maxCiteDepth` was removed from the citation tree.
- In the Navigation endpoint, `member` starts with the requested citable unit itself.
- The namespace of `dts:wrapper` is `https://w3id.org/api/dts#`.
- Ranges (`start`, `end`) are also available as plain text.
- Requests use the identifiers `https://dracor.org/id/…`, which are the same on all servers.

Tag: will be set with the release.

### Version 1: DTS "unstable" (2025)

The first version of this notebook was developed in the context of the project [CLS INFRA](https://clsinfra.io) (Computational Literary Studies Infrastructure). It is an executable version of the chapter:

> Börner, Ingo. "Implementing the Standard API Specification DTS in DraCor for Enhanced Data Access." In *CLS INFRA D7.4 Report on the Implementation of Programmable Corpora*, edited by Ingo Börner and Peer Trilcke, 56–94. Zenodo, 2025. https://doi.org/10.5281/zenodo.15301341

It uses the version of the DTS specification tagged "unstable" (DraCor API 1.1 to 1.4).

Tag: [`2026-11-15-baseline`](https://github.com/dracor-org/dracor-notebooks/tree/2026-11-15-baseline/dts), archived on Zenodo: [10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155). The notebook is unchanged since commit `c13d561` (2025-07-01).
