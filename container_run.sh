#!/bin/bash
DIR=$(cd $(dirname ${0}) && pwd)

docker build -t shadowassist $DIR
docker run -ti -p "8080:5000" -v ${DIR}/data/:/opt/data/ --rm --name shadowassist shadowassist 
