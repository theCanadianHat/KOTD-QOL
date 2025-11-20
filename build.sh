#!/bin/bash
hash=$(git rev-parse HEAD)
echo "${hash}" > version.txt
buildTime=$(date +"%Y-%m-%d_%H:%M:%S") >> version.txt
echo "${buildTime}" >> version.txt
echo "Build Info:"
echo -e "\tCommit Hash: ${hash}"
echo -e "\tBuild Time: ${buildTime}"


if [ -d "venv/Scripts" ]; then
    source venv/Scripts/activate
    PIP_PATH="venv/Scripts/python.exe -m pip"
elif [ -d "venv/bin" ]; then
    source venv/bin/activate
    PIP_PATH="venv/bin/python -m pip"
else
    PIP_PATH="pip"
fi

$PIP_PATH install -r requirements.txt