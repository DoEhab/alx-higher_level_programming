#!/bin/bash
# return the size of the response in bytes
curl -s "$1" | wc -c
