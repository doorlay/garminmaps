#!/usr/bin/env bash

# Create a virtual environment, download all Python dependencies
python3 -m venv .
source bin/activate
pip3 install pandas garminconnect flask