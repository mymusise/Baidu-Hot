#!/bin/bash
#
#Get data automatically

python3 get.py
git add --all
git commit -c "auto commit"
# git push