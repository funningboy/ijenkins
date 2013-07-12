#!/bin/sh
coverage erase
rm -rf *.xml
nosetests --with-xunit --with-coverage --all-modules --cover-package=. --cover-inclusive \
  --traverse-namespace --process-timeout=1 --logging-datefmt=test_suites --cover-xml-file=demo \
  ./test/test_the_square_chest.py
coverage xml
find . -name "*.pyc" | xargs rm -rf

