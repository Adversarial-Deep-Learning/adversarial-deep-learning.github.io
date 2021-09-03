#!/bin/bash
bash ./scripts/WebsiteGeneration/SparseDownloader.sh
# files should not have spaces !
python3 ./scripts/WebsiteGeneration/generation_script.py
echo "Done generating the website"
rsync -va adl_tutorials/Tutorials/ adl/
rm -rf ./adl_tutorials 
