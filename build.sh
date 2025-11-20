#!/bin/bash
hash=$(git rev-parse HEAD)
echo "${hash}" > version.txt
buildTime=$(date +"%Y-%m-%d_%H:%M:%S") >> version.txt
echo "${buildTime}" >> version.txt
echo "Build Info:"
echo -e "\tCommit Hash: ${hash}"
echo -e "\tBuild Time: ${buildTime}"
./venv/Scripts/pip.exe install -r requirements.txt