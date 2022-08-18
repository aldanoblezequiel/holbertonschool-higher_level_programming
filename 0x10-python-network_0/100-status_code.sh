#!/bin/bash
#Sending URL as an argumen
curl -so /dev/null -w "%{http_code}" "$1"
