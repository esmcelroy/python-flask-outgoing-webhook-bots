# Flask-Based Chatbot Framework

This project details the design of a fairly rudimentary API server, that serves data to chat client endpoints through a Flask server.  

## Structure

    .
    +-- app/
    |   +-- endpoints/
    |   |   +-- __init__.py
    |   |   +-- sample.py
    |   +-- utils/
    |   |   +-- __init__.py
    |   |   +-- msteams_verify.py
    |   +-- __init__.py
    +-- config/
    |   +-- #TODO
    +-- tests/
    |   +-- #TODO
    +-- application.py
    +-- run.py
    +-- test.py
    +-- requirements.txt

### The `app` folder

The `app` folder contains three items:

1. An `endpoints` folder
2. A `utils` folder
3. `__init__.py`

The `endpoints` folder contains a number of python scripts, tied together in its `__init__.py` script. Each of these python scripts takes the form of `sample.py`, and provides an `@api.route` for the Flask server. Each `.py` file is imported at the end of the `__init__.py` file in this directory.

The utils folder contains an `__init__.py` file that imports the msteams script in this directory. Add any future helper scripts as an import into this `__init__.py` file.

### The `config` folder

The config folder will contain environment variables in scripts used to configure various environments. This is on the TODO list for now.

### The `tests` folder

The `tests` folder is currently unused, but will allow for future development of a test suite.

### Other files

The five remaining files are used in configuring and running the application.

- `application.py` provides for quick deployment to an app service platform, like Azure App Service.
- `test.py` is incomplete - TODO
- `run.py` starts the server in a development mode. Use `python run.py` to start the server.
- When writing endpoints that use other python modules, add the new modules to `requirements.txt`
