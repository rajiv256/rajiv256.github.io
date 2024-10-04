#!/bin/bash
echo "First moving the images"
cp _posts/images/* blog/images/
git add -A .
git commit -m "Auto push"
git push origin main
