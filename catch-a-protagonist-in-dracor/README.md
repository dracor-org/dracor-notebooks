---
titles:
  main: To catch a protagonist in DraCor
authors:
  -
    name: Ingo Börner
    email: ingo.boerner@uni-potsdam.de
    institution: Universität Potsdam
    orcid: 0000-0001-8294-2541
folder: catch-a-protagonist-in-dracor
date: 2021-11-19
abstract: The notebook "To catch a protagonist in DraCor" adapts the algorithm to identify quantitatively dominant characters presented in the paper "To catch a protagonist" by Fischer et al. for the DraCor API.
language: en
programming_language: Python
packages_required:
  - requests
  - pandas
license: CC BY
---

# To catch a protagonist in DraCor

In the paper [*To catch a Protagonist: Quantitatice Domninance Relations in German-Language Drama" (1730-1930)*](https://dh-abstracts.library.cmu.edu/works/6281) (Fischer et al. 2018) an algorithm is described, that allows to identify characters that are the quantitatively dominant characters of a play based on a set of network-based and count based measures:

> In order to systematically describe the extent of this deviation, we calculate eight values for each character of the 465 dramas of our corpus, three count-based measures (number of scenes a character appears in, number of speech acts, number of spoken words) and five network-related measures (degree, weighted degree, betweenness centrality, closeness centrality, eigenvector centrality). For each measurement a ranking is created. The rankings are then merged into two meta-rankings: one count-based and one network-based. The two meta-rankings are then combined into an overall ranking.

The original algorithm was implemented in the tool [Dramavis](https://github.com/lehkost/dramavis) by [Christopher Kittel](https://github.com/chreman). 

The following notebook adapts the code of the respective modules to work with data returned by the [DraCor API](https://dracor.org/doc/api). The aim is to be able to recreate the `*_chars.csv`-files that were used in the study.

## Bibliography
Fischer, Frank, Peer Trilcke et al. „To Catch a Protagonist: Quantitative Dominance Relations in German-Language Drama (1730–1930)“. DH2018: »Puentes/Bridges«. 26–29 June 2018. Book of Abstracts / Libro de resúmenes, Red de Humanidades Digitales A. C., 2018, https://dh2018.adho.org/to-catch-a-protagonist-quantitative-dominance-relations-in-german-language-drama-1730-1930/.
