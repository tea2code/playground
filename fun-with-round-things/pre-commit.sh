#!/bin/sh
python test.py
RESULT=$?

if [ $RESULT -ne 0 ]; then
    echo "Doctests failed with:\n $RESULT"
    exit 1
fi