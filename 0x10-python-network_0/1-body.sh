#!/bin/bash
#Display the successful response
curl -s "$1" | grep -q "200" && curl -s "$1"
