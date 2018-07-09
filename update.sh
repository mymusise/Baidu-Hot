#!/bin/bash
#
#Get data automatically

git checkout .
git pull
python3 get.py
git add --all
git commit -m "auto commit"
git push
