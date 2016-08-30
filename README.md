FIWARE Validator
======================

[![License](http://img.shields.io/:license-apache-blue.svg?style=flat-square)](http://www.apache.org/licenses/LICENSE-2.0.html)
[![Documentation badge](https://img.shields.io/badge/docs-stable-brightgreen.svg?style=flat)](doc/source/adminmanual.rst)
[![StackOverflow](https://img.shields.io/badge/support-sof-yellowgreen.svg)](https://stackoverflow.com/questions/tagged/fiware-validator)

**Table of Contents**

- [Description](#description)
- [Features Implemented](#features-implemented)
- [Installation Manual](#installation-manual)
- [Installation Verification](#installation-verification)
- [User Manual](#user-manual)
- [API Documentation](#api-documentation)
- [License](#license)
- [Getting Started](#getting-started)
- [Installing Dependencies](#installing-dependencies)
- [Executing the listener API](#executing-the-listener-api)
- [External Dependencies](#external-dependencies)
- [Validation Process](#validation-process)
- [Example Client](#example-client)
- [Image generation](#image-generation)

Description
-----------
This project is part of [FIWARE] (http://fiware.org).

A FIWARE validator for testing deployment artifacts implemented as a Web UI/Restful API pair.

Features Implemented
--------------------
A RESTful API for deployment artifacts validation
A backbone.js based WebUI for FIWARE Lab user interaction.

Installation Manual
-------------------
The installation manual is provided in rst format in the [Installation and Administration manual](doc/source/adminmanual.rst)

Installation Verification
-------------------------
The sanity check procedures are detailed in the [Installation and Administration manual](doc/source/adminmanual.rst)

User Manual
-----------
The user manual is provided in rst format in the [User and Programmers manual](doc/source/usermanual.rst)

API Documentation
-----------------

The API definition can be found at <http://docs.validatorapi2.apiary.io/#>

License
-------

Apache License Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>

Getting Started
---------------

To run the code you can clone the git repo with:

    git clone git@github.com:ging/fiware-validator.git

Installing Dependencies
-----------------------

To install package dependencies you must run:

    pip install -r requirements.txt

Executing the listener API
--------------------------

The listener api can be manually launched with the following command:

    validator-api/manage.py <<URL:PORT>>


External Dependencies
---------------------

The system deployment depends on several external services for
successful completion. The dependency list reads as follows:

- **FIWARE Identity Manager**: Used for issuing user tokens for several OpenStack services
- **Docker Server**: Used for managing the chef server image


Validation Process
------------------

The validation process consists on the following steps:
1. The User interacts with the **WEB UI**, indicating:
    - Authentication credentials.
    - Github Reposity to get a new deployment artifact.
    - Deployment artifact placed in current server user Git repository.
    - Desired Operating System against which to validate.

2. The **WEB UI** sends a POST request to the service API, containing all the pertaining data.

3. The **API** receives the request and takes the following steps:
    - Checks the user permissions to take the next steps by validating against the IdM
    - Downloads the needed *dependencies*
    - Deploys the selected *container* image
    - Instructs the **Deployment Server** to deploy the *artifact* in the given *container*
    - Responds to the **Client** request informing of the status of the validation process

Example Client
---------------
An example client is provided in command/validator-client. It can be run with the following command:

    bork/command/validator-client.py --validator_url=${url_of_the_validator_api} --username=${username} --password=${password} --image=${author/image_name} --cookbook=${cookbook_name}

Image generation
---------------------
A default chef-solo image can be automatically generated and uploaded to the glance server with the following command:

    bork/command/generate_image.py --username=${username} --password=${password} --auth_url={$auth_url} --tag=${author/image_tag} --config-dir {configuration_dir}

Identically, a default puppet-standalone image can be automatically generated and uploaded to the glance server with the following command:

    bork/command/generate_image.py --username=${username} --password=${password} --auth_url={$auth_url} --tag=${author/image_tag} --config-dir {configuration_dir}
