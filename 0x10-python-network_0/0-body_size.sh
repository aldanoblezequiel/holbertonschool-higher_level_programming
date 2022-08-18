#!/bin/bash
#Requesting URL and displaying size of body response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
