#!/usr/bin/env bash
cd $(dirname $0)
if [[ -n $fulltest ]];then
    rm -rf etc src
    rm -rf src/testcgwb testcgwb docs
fi
mkdir tmp
cd tmp
tar xzvf $(ls -1rt ~/cgwb/testcgwb*z|head -n1)
rsync -azv ./ ../
cd ../
rm -rf tmp
if [[ -z $no_clean ]];then
    rm -rf .installed.cfg downloads/ .mr.developer.cfg parts/ bin/ develop-eggs/ eggs/*egg
fi
