# OpenFisca PF

This is the package modeling the French Polynesia rules from https://lexpol.cloud.pf/ :

- Tax system from DICP service (CST-S, IT, CST-NS, TVA, property tax)
- Pricing for the French Polynesia estate management for the public domain and its own lands from DAF service.
- Employees rule from SEFI service.

But this is a work in progress.

## 1. Installation for developers and maintainers

### 1.1. Prerequisites

Serving the OpenFisca WEB API is not currently supported on Windows computer.
It can only be run natively on macOS and Linux.
Thus, on Windows computers a virtual machine is required (pyenv will not suffice).
On Windows, we recommend installing Linux on Windows using Microsoft WSL2:
https://learn.microsoft.com/fr-fr/windows/wsl/install

In the rest of this README we assume that on Windows WSL2 is used.
Any command we describe must thus be executed in a wsl terminal.
To open a wsl terminal, run CMD or PowerShell and run the command:

```bash
wsl
```

### 1.2. Cloning OpenFisca-PF

Clone openfisca-pf project and go to its folder:

```bash
git clone https://github.com/openfisca/openfisca-pf.git
cd openfisca-pf
```

### 1.3. Installing Python 3.13 in a virtual environment

OpenFisca PF requires Python 3.13.
The dependencies are installed in a virtual environment located in the `.venv` folder of the project,
so that they do not interfere with the system Python.

#### Option A: system package

On `macOS` use `homebrew` to install python 3.13:

```bash
brew install python@3.13
```

> See https://formulae.brew.sh/formula/python@3.13 for more details.

On `Linux` or `Windows WSL2` run the following commands:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.13 python3.13-venv
```

> See https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa for more details.

Then create and activate the virtual environment:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

The virtual environment must be activated (`source .venv/bin/activate`) in every new terminal.

#### Option B: mise

Alternatively, [mise-en-place](https://mise.jdx.dev/) installs Python 3.13 without touching the system,
and activates the virtual environment automatically when entering the project folder.
The configuration is defined in the `mise.toml` file of the project.

Install mise and activate it in your shell (see [mise | Getting started](https://mise.jdx.dev/getting-started.html) for other shells).

Then, in the project folder:

```bash
mise trust
mise install
```

#### Check

Make sure the Python in use is the one of the virtual environment:

```bash
which python       # → .../openfisca-pf/.venv/bin/python
python --version   # → Python 3.13.x
```

### 1.4. Installing the dependencies

Install the local project as a python package under development, with OpenFisca Core 43.5.0 and the development tools:

```bash
pip install --editable '.[dev]'      # Option A
uv pip install --editable '.[dev]'   # Option B: the virtual environment created by mise has no pip, use uv
```

> The quotes around `.[dev]` are required with `zsh`.

This command makes `pip` install a package bound to a local directory instead of downloading it from the web.
This way if you modify the openfisca-pf code, your changes will be taken into account on the fly.

Make sure the OpenFisca scripts are the ones of the virtual environment:

```bash
which openfisca    # → .../openfisca-pf/.venv/bin/openfisca
```

### 1.5. Patching OpenFisca Core

In French Polynesia, amounts are expressed in Pacific Franc (XPF) and can become very large.
Thus, they can reach large values that can lead to computation errors when using a 32-bit floating point number.
For this reason OpenFisca Core must be patched to use 64-bit numbers instead of 32-bit ones:

```bash
./patch_openfisca_core.sh
```

The script patches the `openfisca_core` installed in the `.venv` virtual environment
(another virtual environment can be given as argument: `./patch_openfisca_core.sh path/to/venv`).

> The patch must be applied again each time OpenFisca Core is reinstalled or upgraded.

## 2. Running OpenFisca PF

### 2.1. Run tests

You can run tests of the OpenFisca PF country package using:

```bash
openfisca test --country-package openfisca_pf openfisca_pf/tests
```

### 2.2. Serve the API

And you can serve the Openfisca Web API locally (for more information visit the [documentation](https://openfisca.org/doc/openfisca-python-api/openfisca_serve.html)):

```bash
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

## 3. Shortcuts with mise tasks

### 3.1. Prerequisite

The following steps require [mise](https://mise.jdx.dev/) to be installed and activated in your shell,
as described in the [mise installation guide](https://mise.jdx.dev/getting-started.html)
(or in section [1.3. Option B](#option-b-mise)).

### 3.2. Available tasks

The tasks are defined in the `mise.toml` file of the project, like scripts in a `package.json` with npm.
They always run with the Python 3.13 virtual environment of the project.

> The mise tasks are meant for local development.
> The `Makefile` is used by the CI (`.github/workflows`) and the Docker image: its targets are not meant to be run locally
> (`make test` edits the global git configuration and `make serve-local` replaces the editable install with a built package).

| Command            | Equivalent to                                                         |
| ------------------ | --------------------------------------------------------------------- |
| `mise run install` | `uv pip install --editable '.[dev]'` then `./patch_openfisca_core.sh` |
| `mise run test`    | `openfisca test --country-package openfisca_pf openfisca_pf/tests`    |
| `mise run lint`    | `flake8` on the python files tracked by git                           |
| `mise run serve`   | `openfisca serve --reload -f config.py`                               |

List the available tasks with:

```bash
mise tasks
```

The `test` task accepts an optional tests file or folder (`openfisca_pf/tests` by default), for instance to run only the TVA tests:

```bash
mise run test openfisca_pf/tests/dicp/tva
```
