#!/bin/bash
#Requesting 0000500 and causing server response messag
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
