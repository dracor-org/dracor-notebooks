# ExploreCor Showcases: Using DraCor

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fexplorecor-showcases.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fexplorecor-showcases.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

This Jupyter notebook is material from the CLS INFRA Training School **"ExploreCor: Using Programmable Corpora in Computational Literary Studies"** (Vienna, 10–12 June 2024). The name *ExploreCor Showcases* refers to this training school. The training school is documented on [DARIAH-Campus](https://campus.dariah.eu/resources/events/explore-cor-using-programmable-corpora-in-computational-literary-studies), and its material is in the repository [dracor-org/dracor-explorecor](https://github.com/dracor-org/dracor-explorecor).

The notebook shows what can be done with DraCor as a *Programmable Corpus*. The showcases come from chapter 4 of the CLS INFRA report D7.1 *On Programmable Corpora* (Börner and Trilcke 2023, [10.5281/zenodo.7664964](https://doi.org/10.5281/zenodo.7664964), pp. 14–21):

1. a one-click download of modelled text data (§4.1);
2. extracting stage directions for NLP (§4.3);
3. plotting network measures for thousands of plays (§4.4).

The showcase on mapping the locations of first performances with SPARQL and Wikidata (§4.2) is left out for now.

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). The server is set in the variable `api_base` at the beginning of the notebook. Showcase 3 loads the metadata of all corpora on the server, which takes a few minutes.

## Image credits

| File | Content | Source |
|---|---|---|
| `images/fulltext-view.png` | Full text view of a play in the DraCor front end | Screenshot of [dracor.org](https://dracor.org), 2024 |
| `images/download-tab.png` | The "Downloads" tab of a play in the DraCor front end | Screenshot of [dracor.org](https://dracor.org), 2024 |
| `images/gephi-oneclick-networkgraph.png` | Network of a DraCor play visualised in Gephi | D7.1, Fig. 03 |
| `images/sentence-length-datagraph.png` | Mean sentence length in stage directions and spoken text in GerDraCor, from the study by Trilcke et al. 2020 | D7.1, Fig. 05 |
| `images/d71-fig06-average-path-length.png` | Average path length of 2,622 plays, 1500–1900 | D7.1, Fig. 06 |

D7.1: Börner, Ingo, and Peer Trilcke. *CLS INFRA D7.1 On Programmable Corpora*. Zenodo, 2023. https://doi.org/10.5281/zenodo.7664964 (CC BY 4.0).

## Version history

### Version 2: DraCor API v1, PyDraCor 3 (November 2026)

Adapted for the DraCor Notebooks:
- All API calls use PyDraCor 3 and the public DraCor API v1.
- Showcase 3 uses the current metadata of all corpora on the server instead of a fixed corpus, and records the corpus versions (commits).
- Showcase 2 compares the sentence lengths of the stage directions with those of the spoken text.
- The showcase on SPARQL (D7.1, §4.2) is left out for now.
- The parts that referred to the sessions and the setup of the training school are removed.

Drafted with Claude Code (Anthropic) and reviewed by the authors.

Tag: will be set with the release.

### Version 1: ExploreCor Training School (June 2024)

Notebook `1-3_DraCor_Showcase.ipynb`, "1.3 Using DraCor: Four Showcases", by Ingo Börner for the session "Introduction to Programmable Corpora" (10 June 2024) of the CLS INFRA Training School "ExploreCor: Using Programmable Corpora in Computational Literary Studies", Vienna, 10–12 June 2024. Based on D7.1, ch. 4. It ran in the local environment of the training school.

Last state: [dracor-org/dracor-explorecor, commit 40fc0fe](https://github.com/dracor-org/dracor-explorecor/blob/40fc0fe/notebooks/1_Introduction/1-3_DraCor_Showcase.ipynb) (10 June 2024).

Slides of the session: Börner, Ingo. *Introduction to Programmable Corpora: Using DraCor – Showcases*. Zenodo, 2024. https://zenodo.org/records/15111803.
