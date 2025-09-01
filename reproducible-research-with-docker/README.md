# Reproducible Research with Docker 
A *DraCorOS Training Session* at the [DraCor Summit 2025](https://summit.dracor.org) by Ingo Börner

**Abstract:** This training session demonstrates how to establish reproducible research workflows using Docker to create local instances of the DraCor infrastructure, enabling researchers to work with fixed, versioned corpus data. Participants will learn to set up and populate a containerized DraCor environment with specific versions of custom corpora, addressing the fundamental challenge that DraCor’s “living corpora” continuously evolve over time, making repeating research difficult.

## Execute the Notebook

Please make sure you install [Docker Desktop](https://www.docker.com/products/docker-desktop/) on your machine! This should be executed locally. Using Binder or Colab will probably not work well because of the missing Docker installation. Prefeably use a local Jupyter Lab instance:

From within the cloned folder of this notebook execute the following commands:

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

To add the kernel with the dependencies to your Jupyter lab instance and the environment activated use:

```
sudo python3 -m ipykernel install --name reproducible-research-with-docker
```

It is recommended to create a GitHub Access Token beforehand. The token does not need any special rights but you need to authenticate against the GitHub API to have a higher API use limit compared to an anonymous use of the GitHub API.

To create a Personal Access Token log into your GitHub Account and go to `Settings > Developer Settings > Personal Access Tokens > Tokens (classic)` ([GitHub Settings](https://github.com/settings/tokens)). Click on `Generate new token` and select `Generate new token (classic)`. 

You don't have to select any of the boxes, just scroll down and create the token. Don't forget to copy the token (it is the text starting with `ghp...`).

You can either use the token directly in your notebook:

```
dracor = StableDraCor(github_access_token="ghp_12345...")
```

But be careful, your token is like a password and if you want to share your notebook (e.g. add it to a public repo on GitHub) you should not add your token directly to the code. It is safer to use an environment variable for that.

When starting Jupyter Lab you can pass the environment variable:

```
GITHUB_TOKEN=yourtoken jupyter lab
```

## Acknowledgements

In the context of CLS INFRA, the project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No. 101004984.

We acknowledge the OSCARS project, which has received funding from the European Commission’s Horizon Europe Research and Innovation programme under grant agreement No. 101129751.

