# Skyhook Demo

This is a demo for skyhook. It is split into 3 applications:

* **skyhook**: Express.js API with one endpoint. It receives gathered data and, for demo purposes, prints some
  information to the console.
* **crawler**: NodeJs application which represents a crawler. For this demo it reads data from a file and sends it to
  **skyhook**.
* **scraper**: Same as **crawler** but written in Python.

## Table of contents
* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)

## Installation

This demo was meant for running in docker but can also be run manually.

### Docker

To run this demo in docker, you need **docker** and **docker-compose** to be installed on your machine.

### Manual

To run this demo manually you need the following installed on your machine:

* **Python 3**
    * **requests**: `pip3 install requests` or <nobr>`pip install requests`</nobr>
* **NodeJs**
    * Dependencies for the **NodeJs** applications can be installed by running
      `npm install` in <nobr>`<root folder>/crawler/`</nobr> and <nobr>`<root folder>/skyhook/`</nobr>

## Usage

To run this demo, run **skyhook** in a separate terminal from **crawler** and **scraper**. If all goes well, you should
see request information in the output of **skyhook** ever time you run one of the other applications.

### Docker

All commands should be run in the root folder of the project.

* **skyhook**: `docker-compose up skyhook`
* **crawler**: `docker-compose run --rm crawler`
* **scraper**: `docker-compose run --rm scraper`

### Manual

To run each application, all commands should be run in their respective folder i.e. 
<nobr>`<root folder>/<application>/`</nobr>

* **skyhook**: `node app.js`
* **crawler**: `node app.js`
* **scraper**: `python3 main.py` or `python main.py`

## Configuration

Configuration is done via environment variables. For manual use there are fallback values for each variable.

### Docker

All values are defined in the `.env` file. If you change `SKYHOOK_PORT` make sure you change the `ports:` and `expose:`
properties in `docker-compose.yml`.

### Manual

To change configuration when running the demo manually, the fallback values should be changed. These are defined in
the `app.js` and `main.py` files. When changing any fallback for an environment variable starting with `SKYHOOK_`, make
sure to change it in all applications.