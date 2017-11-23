#!/usr/bin/env bash

gogenes.py $@ | grep -v "No results to return"
