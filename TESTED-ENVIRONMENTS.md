# Tested environments

State of the notebooks on `main` at commit `b2125c7`, tested on **2026-11-15**, without changes to the notebooks.

APIs at the time of testing:

| Server | Base URL | Version |
|---|---|---|
| Production, API v1 | `https://dracor.org/api/v1` | 1.4.1 |
| Production, legacy API v0 | `https://dracor.org/api/` (redirects to `/api/v0/`) | 0.91.3 |
| Staging, API v1 | `https://staging.dracor.org/api/v1` | 1.5.0-rc.1 |

For each notebook, `environments/<notebook>.txt` holds the exact package set (`pip freeze`) it was run with. To reproduce a run:

```sh
uv venv --python 3.11 .venv-test        # 3.13 for dts
uv pip install --python .venv-test/bin/python -r environments/<notebook>.txt
```

Runs were headless (`jupyter nbconvert --execute`, one isolated virtual environment per notebook). For notebooks that ask for input, the answers are listed under "Inputs".

## Overview

| Notebook | API | Server | PyDraCor | Python | Result |
|---|---|---|---|---|---|
| `api-tutorial` | v1 | production | – | 3.11 | 35 of 38 cells run. Gender part fails, see notes |
| `catch-a-protagonist-in-dracor` | v1 | production | – | 3.11 | runs |
| `dts` | v1 | staging | – | ≥ 3.12 (tested with 3.13) | 5 errors against staging 1.5.0-rc; see notes |
| `genre-analysis` | **v0**, unversioned `/api/` | production | – | 3.11 | runs, **only through the v0 redirect** |
| `stylometric-text-classification` | **v0**, unversioned `/api` | production | – | 3.11 | runs, **only through the v0 redirect** |
| `speech_analysis` | v1 | production | – | 3.11 | runs |
| `contrastive-text-analysis` (scattertext) | v1 via PyDraCor | production | **2.0.0** (fails with 3.x) | 3.11 | fails: `gender` key, see notes |
| `parts_of_speech` | v1 via PyDraCor | production | **2.0.0** (fails with 3.x) | 3.11 | fails: play renamed, see notes |
| `gender-visualization/fetch_data` | v1 via PyDraCor | production | **2.0.0** (fails with 3.x) | 3.11 | runs, but takes about 30 h (≈ 2.5 min per play, 788 plays) |
| `gender-visualization/dracor_visualization` | v1 via PyDraCor | production | **2.0.0** (fails with 3.x) | 3.11 | fails: `Gender` attribute, see notes |
| `gender-visualization/relationship_network` | none (reads `fetch_data` output) | – | (env of `dracor_visualization`) | 3.11 | fails: `Gender` attribute, see notes |
| `reproducible-research-with-docker` | v1 | local + staging | see its own `requirements.txt` | 3.13 | not part of this test, tested separately |

## Notes per notebook

### `api-tutorial`
- Inputs: corpus `swe`, play `strindberg-gillets-hemlighet` (the notebook's own fallback values).
- Cells 32, 33 and 38 fail with `KeyError: 'gender'`. API v1 returns the values MALE/FEMALE/UNKNOWN in the field `sex`. `gender` is a separate, optional field, and SweDraCor does not set it.

### `catch-a-protagonist-in-dracor`
- Runs without errors.

### `dts`
- Needs Python ≥ 3.12 (nested quotes in f-strings). With 3.11 the notebook stops with a `SyntaxError`.
- Uses staging throughout: the variable `api_base` and many hard-coded URLs and IDs. According to the notebook text, it was written against API 1.1.
- Against staging 1.5.0-rc.1 there are 5 errors (cells 33, 43, 53, 54, 78). The DTS responses have changed: `dublinCore.title` is now a list of `{lang, value}` objects, and the cite structures are different. The outputs stored in the notebook come from the earlier staging state.
- Diagnostic only: with all staging URLs replaced by production (1.4.1), 2 errors remain (cells 53 and 54). They depend on the data, because production `ger000001` has no `front/div[2]`.

### `genre-analysis`
- Inputs: corpus `ger`, no filter (`exit`), interval size `30`, threshold `5`.
- Runs, but uses the unversioned `/api/corpora/`. It will break when v0 is shut down.

### `stylometric-text-classification`
- Runs, but uses the unversioned `/api` and the old `"dramas"` key. It will break when v0 is shut down.

### `speech_analysis`
- Inputs: corpus `ger`, play `goethe-faust-in-urspruenglicher-gestalt`.
- spaCy model `de_core_news_sm` 3.8.0.

### `contrastive-text-analysis` (scattertext)
- With PyDraCor 3.x: `Play(play_name=…)` no longer exists.
- With PyDraCor 2.0.0, cell 4 fails with `KeyError: 'gender'`, the same `sex`/`gender` change as in `api-tutorial`.
- `scattertext` 0.2.2 imports `six` without declaring it as a dependency, so it has to be installed explicitly.
- spaCy model `de_dep_news_trf` 3.8.0 (pulls in PyTorch).
- Diagnostic only: with `c["gender"]` replaced by `c["sex"]`, the notebook runs without errors.

### `parts_of_speech`
- With PyDraCor 3.x: `Play(play_name=…)` no longer exists.
- With PyDraCor 2.0.0: the play `a-midsummer-night-s-dream` is now called `a-midsummer-nights-dream`.
- Diagnostic only: with the new name, the notebook runs without errors.

### `gender-visualization`
- With PyDraCor 3.x, `Corpus('ger')` and `Play(id)` fail.
- With PyDraCor 2.0.0, `fetch_data` works, but very slowly. It was stopped after 30 minutes with 7 plays fetched. `relationship_network` was tested on these 7 plays.
- In `dracor_visualization` and `relationship_network`, the GraphML node attribute is now `Sex`, not `Gender`. A plain search and replace is not enough, because the notebooks also use `Gender` as a column name of their own.

### `reproducible-research-with-docker`
- Not part of this test. It is tested separately. Its pinned environment is in `reproducible-research-with-docker/requirements.txt`.
