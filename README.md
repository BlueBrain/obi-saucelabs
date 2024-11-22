# Test Framework based on: Selenium, Python (pytest) - Page Object Model (POM)
## This test framework is integrated with SauceLabs

## Features
- The tests use setup/teardown methods for the session. 
- Test with Chrome, Firefox and other browsers available in Sauce Labs (also in headless).
- Possibility to view the execution of the test run.
- Possibility to see the screenshots of the errors.
- Live test report in the Sauce Labs platform.

## Install

### Prerequisites:
- Python 3.x installed
- pip package manager installed
- Make sure pip is installed in your system (please see the instructions below).
- Install virtual environment.
- A json file with login credentials would need to be created.  

**Linux/Unix:**
- Run `sudo apt update && sudo apt install python3-pip`

### Setting Up Virtual Environment:
It's recommended to use a virtual environment to manage dependencies. Follow these steps:

**Windows/Linux/Unix:**
1. Install virtualenv if not already installed: 
    ```
    pip install virtualenv
    ```
   or use Python's built-in venv module:
    ```
    python -m venv myenv
2. Create a virtual environment:
    ```
    virtualenv myenv
    ```
3. Activate the virtual environment:
    - **Windows:**
        ```
        myenv\Scripts\activate
        ```
    - **Linux/Unix:**
        ```
        source myenv/bin/activate
        ```
4. Upgrade pip:
    ```
    python -m pip install --upgrade pip
    ```
5. Install dependencies
    ```
    pip install -r requirements.txt
    ```
   
Make sure to replace `myenv` with your preferred name for the virtual environment.

### JSON File for Login Credentials:
Create a JSON file with login credentials to authorize test execution.


### Running Tests:

To run the tests using pytest. Navigate to the directory containing your test files and run:
   ```
   pytest tests -sv or pytest --headless tests -s -v --cache-clear
   ```

### Accessing the reports and screenshots
The test report is available and can be viewed immediately after the test run in Sauce Labs


## Building a container
You'll need a working [podman installation](https://podman.io/docs/installation) (or docker, if you insist).

The `Dockerfile` in the root of this repository will give you a very similar container to the one GitLab will use when running the tests: based on `python:3.10` and with some basic software pre-installed.
If you want to make modifications, [the Dockerfile reference](https://docs.docker.com/engine/reference/builder/) is a really useful document.

```
podman build -t tester:1 .
```
(do not forget the dot at the end of the command!)

Once this is done, you'll have a container:

```
> podman image list
REPOSITORY                                                       TAG                   IMAGE ID      CREATED        SIZE
localhost/tester                                                 1                     8ba4d2af1298  9 minutes ago  1.72 GB
```

## Using your local container

You can now run your container interactively. Note that you'll want to bind your checked out source directory into the container, or you'll have to go through the trouble of cloning your repository again inside the container.

`-i` gives you an interactive shell
`-t` allocates a tty, which means your interactive shell experience will be *much* more pleasant :-)

```
> podman run -v .:/tests -ti localhost/tester:1 /bin/bash
```

Now you can run your tests:

```
cd /tests
python -m venv container_venv
source container_venv/bin/activate
pip install -r requirements.txt
export BROWSER_NAME=firefox
pytest -sv tests/test_login.py
```

Note that you'll need to explicitly create a separate venv within the container - the one you may already have in your source directory _will not work_ inside the container as it was created with the full path on your host system.
Exiting the container will stop it immediately. You can start it again with `podman start --interactive --attach <container_id>`

Unless you make changes to the `Dockerfile`, there's no need to rebuild the container - if you mess up, you can just remove your container and start a new one!

`podman ps -a` to show all containers (including stopped ones)
`podman rm <container_id>` to remove a container. You can specify multiple IDs at once
`podman image list` to show containers available on your system
`podman rmi <image_id>` to remove an image

If you do make changes to the `Dockerfile` and want to rebuild your container, either remove the existing image or increase the version number.


## Spelling/Links

This README file has been checked for spelling errors and links have been verified.

## Legal Requirements

### Copyright, Funding & Authors

The development of this software was supported by funding to the Blue Brain Project,
a research center of the École polytechnique fédérale de Lausanne (EPFL), from 
the Swiss government's ETH Board of the Swiss Federal Institutes of Technology.

- **Copyright**: Copyright (c) 2024 Blue Brain Project/EPFL

### Apache-2.0 license
## Apache License, Version 2.0

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)
