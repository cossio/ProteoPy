#!/usr/bin/env bash

$1 ${@:2} | grep -v "No results to return"
