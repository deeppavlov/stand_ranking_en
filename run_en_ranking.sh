#!/bin/bash
source ./env/bin/activate &&
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64/ &&
nohup python3 ranking_en_api.py > ./ranking_en.log &