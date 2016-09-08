# Morelia
Slack Bot written in Python

https://en.wikipedia.org/wiki/Morelia_(snake)

## Install

```Bash
pip install morelia
```

or 

```Bash
docker pull ghostsquad/morelia
```

## Usage

You can define which components should be loaded in the `.morelia` file.

```Yaml
effectors:
  - package.effector_name
  - morelia.effectors.slack
sensors:
  - package.sensor_name
  - morelia.sensors.slack
interpreters:
  - package.interpreter_name
  - morelia.interpreters.slack_greetings
```

Ensure that other effectors, sensors and interpreters are installed or can be found in `PYTHONPATH`.

### Docker

Run a morelia docker container with out external packages installed.

```Bash
docker run -d -e PYTHONPATH=/opt/ -v /path/to/mypkg:/opt/mypkg -v $(pwd)/.morelia:/.morelia ghostsquad/morelia
```

To create a morelia bot without mounting, and with external packages, you need to build a new image like so...

Given the following directory structure for your morelia bot
```Bash
.
|-- .morelia
|-- my_awesome_bot
    `-- __init__.py
```

Your `Dockerfile` should look like this

```Dockerfile
FROM ghostsquad/morelia
ENV PYTHONPATH=/opt/
RUN pip install <something>
WORKDIR /opt
COPY . /opt
```

Then you can run

```Bash
docker run -d my_awesome_bot
```