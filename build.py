#!/usr/bin/python

import os,re,sys
import json


websites = {}
currentDir = os.path.dirname(os.path.abspath(__file__))
extension = '.browsernav-website'
outputFile = os.path.join(currentDir, 'output', 'websites.json')
for fileName in os.listdir(currentDir):
    if not fileName.endswith(extension):
        continue
    j = json.loads(open(fileName, 'r', encoding='utf-8').read())
    name = j['name']
    if fileName != f"{name}{extension}":
        print(f"Build error: file {fileName} contains website definition with a different name {name}. Please rename either the file or website fefinition so that they match. ")
        sys.exit(1)
    websites[name] = {
        'website': j,
    }


j = {
    'websites': websites,
}
f = open(outputFile, 'w', encoding='utf-8')
try:
    s = json.dumps(j, indent=4, sort_keys=True)
    print(s, file=f)
finally:
    f.close()

print("Successfully built websites in local repository ! Now please create a PR to submit your change.")
