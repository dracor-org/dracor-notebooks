# Words in a Play

[![Status on dracor.org](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fparts_of_speech.production.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html) [![Status on staging](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdracor-org%2Fdracor-notebooks%2Fmain%2Fstatus%2Fbadges%2Fparts_of_speech.staging.json)](https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html)

This Jupyter notebook loads the spoken text of Shakespeare's *A Midsummer Night's Dream* ([ShakeDraCor](https://dracor.org/shake/a-midsummer-nights-dream)) with [PyDraCor](https://pypi.org/project/pydracor/), detects the parts of speech with [spaCy](https://spacy.io/) and lists the most frequent parts of speech and the most frequent words (lemmas) per part of speech.

## Running the notebook

Install the required packages with `pip install -r requirements.txt` (Python 3.10 or newer). This includes the English language model `en_core_web_sm` of spaCy. The server is set in the variable `api_base` in the section "load play from DraCor".

**Known problem (November 2026):** PyDraCor 3 cannot load *A Midsummer Night's Dream* yet, because two characters have invalid values in `@sex` in the TEI of ShakeDraCor ([shakedracor#22](https://github.com/dracor-org/shakedracor/issues/22)). The values are corrected in [shakedracor#23](https://github.com/dracor-org/shakedracor/pull/23); the notebook runs once the corrected corpus is loaded on the DraCor server. Until then, the notebook can be tried with another play of ShakeDraCor, e.g. `play_name="the-tempest"`.

## Version history

### Version 2: PyDraCor 3 (November 2026)

Ingo Börner updated the notebook to PyDraCor 3 ([#40](https://github.com/dracor-org/dracor-notebooks/issues/40)):

- PyDraCor 3 has a new interface: the play is retrieved with `DraCorAPI(host=api_base).get_play(corpus_name="shake", play_name=…)` and its spoken text with `get_spoken_text()`. `Play(play_name=…)` of PyDraCor 2 no longer exists.
- The play is now called `a-midsummer-nights-dream` (before: `a-midsummer-night-s-dream`).
- The installation commands are commented out; the packages are listed in `requirements.in` and the lock file, together with the English language model of spaCy.
- The notebook has a short introduction and a metadata block, and the folder this README.

Tested on 2026-11-17 with DraCor API 1.4.1 (production) and 1.5.0-rc.1 (staging), PyDraCor 3.0.2, Python 3.12, with *The Tempest* instead of *A Midsummer Night's Dream* (see "Known problem" above).

Prepared with Claude Code (Anthropic) and reviewed by the author.

Tag: will be set with the release.

### Version 1: PyDraCor 2 (April 2024)

The first version by Robert Jäschke (commit `80b37df`, 2024-04-12) used [PyDraCor](https://pypi.org/project/pydracor/) 2, which uses DraCor API v1. It stopped working with PyDraCor 3 (September 2025, new interface), because the installation of PyDraCor was not pinned, and when the play was renamed.

Tag: [`2026-11-15-baseline`](https://github.com/dracor-org/dracor-notebooks/tree/2026-11-15-baseline/parts_of_speech), archived on Zenodo: [10.5281/zenodo.24237155](https://doi.org/10.5281/zenodo.24237155).
