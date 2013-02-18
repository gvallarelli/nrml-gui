#!/bin/bash

rm resources.py resources.pyc
pyrcc4 -o ./resources.py ./resources.qrc
