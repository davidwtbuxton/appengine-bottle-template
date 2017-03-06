#!/bin/bash

set -o nounset -o errexit

ln -s ../../node_modules/bulma {{ cookiecutter.static_dir }}/src/bulma
ln -s ../../node_modules/font-awesome {{ cookiecutter.static_dir }}/src/font-awesome
ln -s ../../node_modules/jquery {{ cookiecutter.static_dir }}/src/jquery
