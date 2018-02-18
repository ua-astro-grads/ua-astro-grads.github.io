#!/usr/bin/env bash

if [ -f .jupyter/jupyter_notebook_config.py ]; then
	jupyter-notebook
else
	jupyter-notebook --allow-root --ip='*' --no-browser
fi
