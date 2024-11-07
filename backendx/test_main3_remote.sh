#!/bin/bash

IP=$(sky status --ip main3)
curl -X GET http://$IP:8000/?val=100.0
