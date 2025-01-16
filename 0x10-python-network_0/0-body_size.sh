#!/bin/bash
#Display the size of the body response
curl -sL "$1" | wc -c

