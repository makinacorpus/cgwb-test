#!/usr/bin/env bash
cd $(dirname $0)
rm -rf etc src
if [[ -n $fulltest ]];then
    tar xzvf $(ls -1rt ~/cgwb/testcgwb*z|head -n1)
    rm -rf src testcgwb
    cd testcgwb || exit -1
    mv -f * .* ..
    cd ..
    rm -rf testcgwb
fi
if [[ -z $no_clean ]];then
    rm -rf .installed.cfg downloads/ .mr.developer.cfg parts/ bin/ develop-eggs/ eggs/*egg
fi
