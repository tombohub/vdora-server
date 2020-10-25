#!/bin/bash

git add .
git commit -m "$1"
git push 


## usage:
## ./git-push.sh 'your commit comment here'