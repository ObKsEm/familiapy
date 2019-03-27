#!/bin/bash
export CPLUS_INCLUDE_PATH=/Users/lichengzhi/miniconda2/include
export LD_LIBRARY_PATH=/Users/lichengzhi/miniconda2/lib

mkdir -p third_party
make deps
make clean && make -j4;
