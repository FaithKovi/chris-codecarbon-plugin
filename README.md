# ChRIS Codecarbon Plugin

[![Version](https://img.shields.io/docker/v/fnndsc/chris-codecarbon-plugin?sort=semver)](https://hub.docker.com/r/fnndsc/chris-codecarbon-plugin)
[![MIT License](https://img.shields.io/github/license/fnndsc/chris-codecarbon-plugin)](https://github.com/FNNDSC/chris-codecarbon-plugin/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/chris-codecarbon-plugin/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/chris-codecarbon-plugin/actions/workflows/ci.yml)

`chris-codecarbon-plugin` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which takes in ...  as input files and
creates ... as output files.

## Abstract

...

## Installation

`chris-codecarbon-plugin` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://ipfs.babymri.org/ipfs/QmaQM9dUAYFjLVn3PpNTrpbKVavvSTxNLE5BocRCW1UoXG/light.png)](https://chrisstore.co/plugin/chris-codecarbon-plugin)

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `chris-codecarbon-plugin` as a container:

```shell
singularity exec docker://fnndsc/chris-codecarbon-plugin codecarbon [--args values...] input/ output/
```

To print its available options, run:

```shell
singularity exec docker://fnndsc/chris-codecarbon-plugin codecarbon --help
```

## Examples

`codecarbon` requires two positional arguments: a directory containing
input data, and a directory where to create output data.
First, create the input directory and move input data into it.

```shell
mkdir incoming/ outgoing/
mv some.dat other.dat incoming/
singularity exec docker://fnndsc/chris-codecarbon-plugin:latest codecarbon [--args] incoming/ outgoing/
```

## Development

Instructions for developers.

### Building

Build a local container image:

```shell
docker build -t localhost/fnndsc/chris-codecarbon-plugin .
```

### Running

Mount the source code `codecarbon.py` into a container to try out changes without rebuild.

```shell
docker run --rm -it --userns=host -u $(id -u):$(id -g) \
    -v $PWD/codecarbon.py:/usr/local/lib/python3.10/site-packages/codecarbon.py:ro \
    -v $PWD/in:/incoming:ro -v $PWD/out:/outgoing:rw -w /outgoing \
    localhost/fnndsc/chris-codecarbon-plugin codecarbon /incoming /outgoing
```

### Testing

Run unit tests using `pytest`.
It's recommended to rebuild the image to ensure that sources are up-to-date.
Use the option `--build-arg extras_require=dev` to install extra dependencies for testing.

```shell
docker build -t localhost/fnndsc/chris-codecarbon-plugin:dev --build-arg extras_require=dev .
docker run --rm -it localhost/fnndsc/chris-codecarbon-plugin:dev pytest
```

## Release

Steps for release can be automated by [Github Actions](.github/workflows/ci.yml).
This section is about how to do those steps manually.

### Increase Version Number

Increase the version number in `setup.py` and commit this file.

### Push Container Image

Build and push an image tagged by the version. For example, for version `1.2.3`:

```
docker build -t docker.io/fnndsc/chris-codecarbon-plugin:1.2.3 .
docker push docker.io/fnndsc/chris-codecarbon-plugin:1.2.3
```

### Get JSON Representation

Run [`chris_plugin_info`](https://github.com/FNNDSC/chris_plugin#usage)
to produce a JSON description of this plugin, which can be uploaded to a _ChRIS Store_.

```shell
docker run --rm localhost/fnndsc/chris-codecarbon-plugin:dev chris_plugin_info > chris_plugin_info.json
```

