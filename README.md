# OpenFisca PF

This is the package modelling the French Polynesia tax system.
What is currently modelled:
- CST-S
- IT

But this is a work in progress and none of those taxes are validated yet.

## Installation for developpers and maintainers

Installation does not work on windows despite using Python, but it is working well in a WSL.
To install it first get the git repo :
```sh
git clone https://github.com/govpf/openfisca-pf.git
```

Then make sure you have all dependencies (this example is for Ubuntu or Debian based distro):
```sh
sudo apt-get update
sudo apt upgrade
sudo apt-get install make python3-pip
```
Pip is named pip 3 in Ubuntu so you should add an alias:
```sh
echo "alias pip='pip3'" >> ~/.bash_aliases
source ~/.bashrc
```

Then you can install openfisca :

```sh
cd openfisca-pf
pip install --editable .[dev] --upgrade
```

Then make sure your openfiscal installation is in your path:
```sh
echo "export PATH=$HOME/.local/bin:${PATH}:" >> ~/.bashrc
source ~/.bashrc
```

## Serve this Country Package with the OpenFisca Web API

To serve the Openfisca Web API locally, run:

```sh
openfisca serve --configuration-file config.py
```

To read more about the `openfisca serve` command, check out its [documentation](https://openfisca.org/doc/openfisca-python-api/openfisca_serve.html).

You can make sure that your instance of the API is working by requesting:

```sh
curl "http://localhost:5000/spec"
```

This endpoint returns the [Open API specification](https://www.openapis.org/) of your API.

:tada: This OpenFisca Country Package is now served by the OpenFisca Web API! To learn more, go to the [OpenFisca Web API documentation](https://openfisca.org/doc/openfisca-web-api/index.html).

You can test your new Web API by sending it example JSON data located in the `situation_examples` folder.

Substitute your package's country name for `openfisca_pf` below:

```sh
curl -X POST -H "Content-Type: application/json" \
  -d @./openfisca_pf/situation_examples/couple.json \
  http://localhost:5000/calculate
```