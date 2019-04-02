#!/bin/bash
echo "python ./build_index.py"
#jekyll build
python ./build_index.py
cp search.json _site/search.json