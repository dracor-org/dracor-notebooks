# Gender representation in German plays

This collection of Jupyter notebooks provides tools to analyze and visualize gender representation in German plays. The primary goal of this project is to provide quantitative insights and inspiration for further research into the dramatic texts included in the German Drama Corpus. By visualizing relationships and gender distribution, researchers can gain a deeper understanding of the dynamics within each play.

## dracor_visualization.ipynb
The `dracor_visualization.ipynb` notebook queries metadata about a selected play from the [DraCor API](https://dracor.org/doc/api) and generates visualizations that offer insights into relationships and gender distribution within the selected drama. These visualizations serve as a starting point for further analysis of the play's themes and characters.

## Fetching Metadata and Visualization
To improve performance and modularity, fetching metadata and generating visualizations can be done separately. Use the `fetch_data.ipynb` notebook to download metadata from the DraCor API, and then use the `relationship_network.ipynb` notebook to visualize the relationships within the selected play.

## Data Source
The German Drama Corpus used in this project is provided by the [Drama Corpus (DraCor) Project](https://dracor.org) as of 08.03.2024.

## Contact
For any inquiries or feedback, please contact Sandra Densch-Glazov at densch.sandra@gmail.com.
