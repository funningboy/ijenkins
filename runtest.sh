#!/bin/sh

nosetests --with-xunit --with-coverage --all-modules --cover-package=project1 --cover-inclusive --traverse-namespace --process-timeout=1 --logging-datefmt=test_suites ./test/test_the_square_chest.py
find . -name "*.pyc" | xargs rm -rf

