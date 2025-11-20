#!/bin/bash
git fetch --unshallow --tags || git fetch --tags
tag=$(git describe --tag --abbrev=0)
echo "${tag}" > version.txt
hash=$(git rev-parse HEAD)
echo "${hash}" >> version.txt
buildTime=$(date +"%Y-%m-%d_%H:%M:%S") >> version.txt
echo "${buildTime}" >> version.txt
echo "Build Info:"
echo -e "\tTag: ${tag}"
echo -e "\tCommit Hash: ${hash}"
echo -e "\tBuild Time: ${buildTime}"
#./venv/Scripts/pip.exe install -r requirements.txt