# OpenFisca PF

This is the package modelling the French Polynesia tax system.
What is currently modelled:
- CST-S
- IT
- CST-NS

But this is a work in progress and none of those taxes are validated yet.

## Installation for developers and maintainers

Install python 3.7
> * Go to https://www.python.org/downloads/release/python-370/
> * Download the python install that suits your OS.
> * Install it.

Make sure that python scripts are in your path.
On windows:
> * Open an explorer window (any folder)
> * Right click `My Computer` (`Ce PC`)
> * Select `Properties` (`Propriétés`)
> * In the new settings window that opens select `Advanced parameters` (`Paramètres avancés du système`).
> * In the new settings window that opens, select `Environment Variables` (`Variables d'environement`).
> * In the top section (variables specific to your Windows user account), select the `Path` variable.
> * Click `Edit` (`Modifier...`)
> * In the new window that opens, click `New` (`Nouveau`). This will add a new line ready for edition.
> * Past the following path `%USERPROFILE%\AppData\Roaming\Python\Python37\Scripts`
> * Click `Ok` to close this window
> * Click `Ok` to close the previous window
> * Click `Apply` and `Ok` to close the first window.

Make sure PIP is up-to-date
```bash
python -m pip install --upgrade pip
```

Install Openfisca Core. This will install the python package, and add some scripts in the folder we added to path above.
```bash
pip3 install openfisca-core[web-api]
```

Go to the folder of the Openfisca PF project
```bash
openfisca-pf
```

Install the local development project as a python package:
```bash
pip3 install --editable .[dev]
```

You are done, you can run tests of the OpenFisca PF using:
```bash
openfisca test --country-package openfisca_pf openfisca_pf/tests
```

And you can serve the Openfisca Web API locally (for more information visit the [documentation](https://openfisca.org/doc/openfisca-python-api/openfisca_serve.html)):
```bash
openfisca serve --configuration-file config.py
```

You can make sure that your instance of the API is working by requesting:
```sh
curl "http://localhost:5000/spec"
```

This endpoint returns the [Open API](https://www.openapis.org/) specification of the Openfisca PF API.
For more details on the wall api see the documentation on the [OpenFisca Web API documentation](https://openfisca.org/doc/openfisca-web-api/index.html).