# Gender Representation in German Plays

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fgender-visualization.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fgender-visualization.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

This collection of Jupyter notebooks provides tools to analyze and visualize gender representation in German plays. The primary goal of this project is to provide quantitative insights and inspiration for further research into the dramatic texts included in the German Drama Corpus. By visualizing relationships and gender distribution, researchers can gain a deeper understanding of the dynamics within each play.

The notebooks were written by Sandra Densch-Glazov, Leonie Wichers, Kyung Yun Choi and Benedikt Schuh.

**Please read the note on sex and gender below.**

## dracor_visualization.ipynb
The `dracor_visualization.ipynb` notebook queries metadata about a selected play from the [DraCor API](https://dracor.org/doc/api) and generates visualizations that offer insights into relationships and gender distribution within the selected drama. These visualizations serve as a starting point for further analysis of the play's themes and characters.

## Fetching Metadata and Visualization
To improve performance and modularity, fetching metadata and generating visualizations can be done separately. Use the `fetch_data.ipynb` notebook to download metadata from the DraCor API, and then use the `relationship_network.ipynb` notebook to visualize the relationships within the selected play.

## A note on sex and gender

The notebooks speak of "gender", but the data they visualise is the **sex** of the characters as encoded in DraCor: the TEI attribute `@sex` with the values `MALE`, `FEMALE` and `UNKNOWN`. When the notebooks were written (2024), the DraCor API returned this value in a property called `gender`.

DraCor has since revised its encoding of sex and gender ([dracor-schema#94](https://github.com/dracor-org/dracor-schema/pull/94), 2025; see also [dracor-schema#46](https://github.com/dracor-org/dracor-schema/issues/46)), following the revision of sex and gender in the TEI Guidelines (Beshero-Bondar et al. 2024). It now distinguishes the sex of a character (`@sex`) from its gender (`@gender`), which is optional and not encoded in most corpora. Since DraCor API 1.1.0 (July 2025), the API returns them as `sex` and `gender` ([dracor-api#319](https://github.com/dracor-org/dracor-api/pull/319)), and the GraphML files of the networks have the attribute `Sex`.

In version 2, the notebooks still label their charts and filters with "gender", but the values shown are those of `Sex`. Keep this in mind when you interpret the visualisations.

Beshero-Bondar, Elisa Eileen, Raffaele Viglianti, Helena Bermúdez-Sabel, and Janelle Jenstad. "Revising sex and gender in the TEI Guidelines". *Journal of the Text Encoding Initiative*, Issue 17 (2024). https://doi.org/10.4000/13utq.

## Running the notebooks

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). The server is set in the variable `api_base` in each notebook.

- `dracor_visualization.ipynb` works on its own: it loads the data of the selected play from the API.
- `relationship_network.ipynb` needs the data downloaded by `fetch_data.ipynb` into the folder `data`. For all plays of GerDraCor, the download takes about 20–25 minutes; to try it with a few plays first, set `max_plays` in `fetch_data.ipynb` to a small number.

## Data Source
The German Drama Corpus used in this project is provided by the [Drama Corpus (DraCor) Project](https://dracor.org). Version 1 of the notebooks used the state of 08.03.2024; version 2 retrieves the current state of the corpus.

## Contact
For any inquiries or feedback, please contact Sandra Densch-Glazov at densch.sandra@gmail.com.

## Version history

### Version 2: PyDraCor 3, current DraCor API v1 (November 2026)

Ingo Börner updated the notebooks to PyDraCor 3 and the current version of the DraCor API v1 ([#41](https://github.com/dracor-org/dracor-notebooks/issues/41)):

- PyDraCor 3 has a new interface: `DraCorAPI(host=api_base).get_corpus("ger")`, `get_metadata()`, `get_play()`, `get_relations(DownloadFormat.graphml)` and `get_networkdata(DownloadFormat.graphml)` replace `Corpus('ger')`, `Play(play_id)`, `relations_graphml()` and `graphml()`.
- The GraphML files have the attribute `Sex` instead of `Gender` (see the note on sex and gender above). The charts use the values of `Sex`.
- `fetch_data.ipynb` loads the list of plays once and requests each play only once. With PyDraCor 2, it requested the whole corpus several times for each play, which made the download take about 30 hours. It has an introduction and the new parameter `max_plays`.
- The notebooks have a metadata block, and the folder a `requirements.in` and a lock file.

Tested on 2026-11-17 with DraCor API 1.4.1 (production) and 1.5.0-rc.1 (staging), PyDraCor 3.0.2, Python 3.12: `fetch_data.ipynb` with the first 40 plays of GerDraCor (14 with relations, about 1 minute), `relationship_network.ipynb` with these data, and `dracor_visualization.ipynb` with Lessing's *Emilia Galotti*.

Prepared with Claude Code (Anthropic) and reviewed by the authors.

Tag: will be set with the release.

### Version 1: PyDraCor 2 (March 2024)

The first version by Sandra Densch-Glazov, Leonie Wichers, Kyung Yun Choi and Benedikt Schuh (commit `420a363`, 2024-03-15), based on [PyDraCor](https://pypi.org/project/pydracor/) 2. Ingo Börner added the title of `dracor_visualization.ipynb` and the notebook to the book (commits `bf58f6f` and `096608e`, 2024-04-04). It stopped working with DraCor API 1.1.0 (July 2025, `gender` renamed to `sex`) and with PyDraCor 3 (September 2025, new interface).

Tag: [`2026-11-15-baseline`](https://github.com/dracor-org/dracor-notebooks/tree/2026-11-15-baseline/gender-visualization), archived on Zenodo: [10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155).
