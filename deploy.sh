#!/bin/bash
git add -A
git commit -m $1
git push origin woolee
chalice deploy --profile makeyourpage