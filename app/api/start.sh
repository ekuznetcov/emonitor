#!/bin/bash
app="splitrestest"
docker build -t ${app} .
docker run -d -p 8080:5000\
    --name=${app} -v ${PWD}:/app ${app}