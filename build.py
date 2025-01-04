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

# Sorting websites by name
websites = {
    name: websites[name]
    for name in sorted(list(websites.keys()))
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

print("Successfully built websites in local repository !")

sitesText = []
for name, website in websites.items():
    sitesText.append(f"### {name}\n")
    sitesText.append(f"* Version {website['website']['version']}")
    sitesText.append(website['website']['description'])
    sitesText.append("\n")
sitesText = "\n".join(sitesText)
readmeTemplateFileName = os.path.join(currentDir, 'README_TEMPLATE.md')
readmeFileName = os.path.join(currentDir, 'README.md')
readmeText = open(readmeTemplateFileName, 'r', encoding='utf-8').read()
readmeText = readmeText.replace("!!!sitesPlaceHolder!!!", sitesText)

f = open(readmeFileName, 'w', encoding='utf-8')
try:
    print(readmeText, file=f)
finally:
    f.close()

print("Successfully updated README.md.")
print("Now please create a PR to submit your change.")
