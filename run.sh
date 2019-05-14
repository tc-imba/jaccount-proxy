#!/bin/bash

export FLASK_DEBUG=True
export FLASK_APP=jaccountproxy
export JACCOUNT_PROXY_SETTINGS=`pwd`/config.py
flask run --host 0.0.0.0 --port 8888
