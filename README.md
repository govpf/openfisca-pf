# OpenFisca PF

This is the package modelling the French Polynesia tax system.
What is currently modelled:
> - CST-S
> - IT
> - CST-NS
> - TVA & CPS

But this is a work in progress and none of those taxes are validated yet.

It includes the pricing for the French Polynesia estate managment for the public domain and its own lands.

See the Confluence documentation here:
> https://doc.projet.gov.pf/pages/viewpage.action?pageId=40938529

## 1. Installation for developers and maintainers

### 1.1. Prerequisites

Serving the OpenFisca WEB API is not currently supported on Windows computer.
It can only be run natively on macOS and Linux.
Thus, on Windows computers a virtual machine is required (pyenv will not suffice).
On Windows, we recommend install Linux on Windows using Microsoft WSL2:
https://learn.microsoft.com/fr-fr/windows/wsl/install

In the rest of this README we assume that on Windows WSL2 is used.
Any command we describe must thus be executed in a wsl terminal.
To open a wsl terminal run CMD or PowerShell and run the command:
```bash
wsl
``` 

### 1.1. Installing Python 3.10

#### macOS

On `macOS` use `homebrew` to install python 3.10:
```bash
brew install python@3.10
```
See https://formulae.brew.sh/formula/python@3.10 for more details.

#### Windows WSL2 and Linux

On `Linux` or `Windows WSL2` Run the following command
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.10
```
> See https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa for more details.

#### Python Scripts 

OpenFisca will install two python scripts to test and serve the API.
So make sure that python scripts are in your path.
This should be the case by default on `Linux` and `macOS`.
On windows add `%USERPROFILE%\AppData\Roaming\Python\Python310\Scripts` to you `PATH`.

### 1.2. Installing and Patching OpenFisca Core

#### Update pip

Make sure PIP is up-to-date
```bash
python3 -m pip install --upgrade pip
```

#### Install Openfisca Core.

Pip install the openfisca core version 40.0.0 with the flask web api.
This will install the python package, and add the two scripts we mentioned above to the python scripts directory.
```bash
pip3 install openfisca-core[web-api]==40.0.0
```

#### Patch OpenFisca Core

In French Polynesia, amounts are expressed in Pacific Franc (XPF) and can become very large.
Thus, they can reach large values that can lead to computation errors when using 32-bit floating point number.
For this reason when need to edit OpenFisca Core tu use 64-bit floating point numbers instead of 32-bit ones.
> - Locate your `openfisca-core` install directory in the `site-package` directory.
>   - On Windows it will be located at one of the two following path:
>     - `%HOMEDRIVE%%HOMEPATH%\AppData\Roaming\Python\Python310\site-packages\openfisca_core`
>     - `%HOMEDRIVE%\Program Files\Python310\Lib\site-packages\openfisca_core`.
>   - On Windows WSL2 it will be located at:
>     - `%HOMEDRIVE%%HOMEPATH%\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\rootfs\usr\local\lib\python3.10\dist-packages\openfisca_core`
>   - On Linux it will be located at:
>     - `$HOMEBREW_PREFIX/lib/python3.10/site-packages/openfisca_core`
> - Open the file `openfisca_core\variables\config.py`.
> - At line `18` and `25`, replace `numpy.int32` to `numpy.int64` and `numpy.float32` to `numpy.float64` 
> - Open the file `openfisca_core/tools/__init__.py`
> - At lines `44` and `46`, replace `numpy.float32` to `numpy.float64`.

### 1.3. Installing OpenFisca-PF

Clone the OpenFisca-PF project:
```bash
wget https://github.com/openfisca/openfisca-core/archive/refs/tags/40.0.0.zip
```

Go to the folder where you clone the Openfisca PF project
```bash
cd openfisca-pf
```

Install the local project as a python package under development:
```bash
pip3 install --editable .[dev]
```
This command makes `pip` install a package bound to a local directory instead of downloading it from the web.
This way if you modify the openfisca-pf code, your changes will be taken into account on the fly.

## 2. Running OpenFisca PF

### 2.1. Run tests

You can run tests of the OpenFisca PF country package using:
```bash
cd openfisca-pf
openfisca test --country-package openfisca_pf openfisca_pf/tests
```

### 2.1. Serve the API

And you can serve the Openfisca Web API locally (for more information visit the [documentation](https://openfisca.org/doc/openfisca-python-api/openfisca_serve.html)):
```bash
cd openfisca-pf
openfisca serve --reload -f config.py
```

> ONLY AVAILABLE ON linux, macOS, and Windows WSL2

To read more about the `openfisca serve` command, check out its [documentation](https://openfisca.org/doc/openfisca-python-api/openfisca_serve.html).

You can make sure that your instance of the API is working by requesting:
```bash
curl "http://localhost:5000/spec"
```

This endpoint returns the [Open API](https://www.openapis.org/) specification of the Openfisca PF API.
For more details on the API see the documentation on the [OpenFisca Web API documentation](https://openfisca.org/doc/openfisca-web-api/index.html).
