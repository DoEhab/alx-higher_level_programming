#!/bin/bash
# return response size in bytes
curl -s "$1" | wc -c

