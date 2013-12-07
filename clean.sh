#!/usr/bin/env bash
cd $(dirname $0)
rm -rf etc src
if [[ -n $fulltest ]];then
    rm -rf testcgwb
    tar xzvf $(ls -1rt ~/cgwb/testcgwb*z|head -n1)
    mv testcgwb orig
    cd orig
    mv -f * .* ..
    cd ..
    rm -rf orig
fi
if [[ -z $no_clean ]];then
    rm -rf .installed.cfg downloads/ .mr.developer.cfg parts/ bin/ develop-eggs/ eggs/*egg
fi
