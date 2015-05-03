#!/bin/bash

args=("$@")
echo $@ 

dpkg -s  $@ | grep 'Version' | awk '{print $2}'

