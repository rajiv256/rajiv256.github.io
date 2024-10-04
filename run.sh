#!/bin/bash

echo "First moving images"
cp _posts/images/* blog/images/
bundle exec jekyll serve
