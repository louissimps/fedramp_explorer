#!/bin/bash
echo "build started......"
#jekyll build
echo "finished jekyll build, start indexing......."
python ./build_index.py
echo "Indexing complete......."
echo "Copy data file to _site"
cp search.json _site/search.json
echo "Syncing _site with s3: folder"
aws s3 sync _site/ s3://fedramp-explorer/ 
echo "Creating new cache invalidation template"

CALLER_REF=$(gdate +%s)
CALLER_JSON=$(sed -e 's/cref/'$CALLER_REF'/g' invalidate-cache.json.template)
echo "invalidating cache with....."
echo $CALLER_JSON
echo $CALLER_JSON > invalidate-cache.json
aws cloudfront create-invalidation  --cli-input-json file://invalidate-cache.json
