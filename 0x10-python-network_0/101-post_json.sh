#!/bin/bash
#Shows respons that takes JSON as an argumen
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
