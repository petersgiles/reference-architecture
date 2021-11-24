---
title: "With Python"
linkTitle: "With Python"
weight: 100
description: >
  How to Create a Python Development Environment with Docker
---

## Problem

- Setup takes ages, I just want to open IDE and Code
- Installation incompatibilities between dev machines
- Lag times to get other developers in a position to review and test code

## Containers as a Solution

- Docker
- Podman

Using a container a developer can create a single-purpose virtual machine. A VM that can be created again and again, whenever a development environment is required.

## Example

### Step 1: Declare Python dependencies

Use one of these tools

- poetry
- venv
- pip
- conda

It's worth reading up on each of these tools to work out which of them suits your needs.

Here is an example conda environment.yml file

```yaml
# run: conda env create --file environment.yml
name: test-env
dependencies:
  - python>=3.5
  - anaconda
  - pip
  - numpy=1.13.3 # pin version for conda
  - pip:
      # works for regular pip packages
      - docx
      - gooey
      - matplotlib==2.0.0 # pin version for pip
      # and for wheels
      - http://www.lfd.uci.edu/~gohlke/pythonlibs/bofhrmxk/opencv_python-3.1.0-cp35-none-win_amd64.whl
```

### Step 2: Write the build instructions

This is how to write a Dockerfile to build a container image, beginning with the version of Python wanted, then adding all of my dependencies to.

Starting with “Docker Official” image from Docker Hub, gives some confidence about its quality and security.

```Docker
FROM python:3.9-alpine

# change the working directory to /usr/src/app.
# This tells Docker where to run the remaining commands.
WORKDIR /usr/src/app

# Next, copy the requirements file that from the previous step, and put it in the container.
# I run the install command, which will download all the needed packages

COPY environment.yml .
RUN conda env create --file environment.yml

```

### Step 3: Build the image

This will create the image that we’ll use when want to develop.

With docker, type:

```bash
docker build -t python-dev:1.0 .
```

Or if you’re using Podman:

```bash
podman build -t python-dev .
```

This will build an image called python-dev.

### Step 4: Run the container

The container image, or Docker image containing Python and the requirements is created.

To start the environment, run a container based on the python-dev image, and tell it to launch a command prompt (sh):

```bash
docker run -it --name myapp --rm \
    --volume $(pwd):/usr/src/app \
    --net=host myapp-dev:latest \
    sh

```

Creating a bind mount `--volume ...` makes the current directory (PWD) on the host operating system available inside the container. This will allows the editing of files on the host, and have them available inside the container, in real-time.

If you’re using SELinux, you might need to add the `:z` modifier to the end, e.g. `--volume $(pwd):/usr/src/app:z`

Giving the container a name `myapp`, because calling containers by their proper names it is easier to understand their purpose.

Adding `--rm`, will delete the container when it terminates (the source code files will still exist on the host OS).

Setting `--net=host`, allows the container to share the local (hosting) network. Allowing Python website access using the localhost address.

### Step 5: Doing the coding

Development activities are available using the docker shell.
