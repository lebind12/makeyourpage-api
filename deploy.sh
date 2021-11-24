#!/bin/bash
git add -A
git commit -m "$1"
git push origin dev
chalice deploy --profile makeyourpage