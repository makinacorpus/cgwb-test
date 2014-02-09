#!/usr/bin/env bash
cd $(dirname $0)
rm -rf etc src
if [[ -n $fulltest ]];then
    tar xzvf $(ls -1rt ~/cgwb/test*cgwb*z|head -n1)
fi
if [[ -z $no_clean ]];then
    rm -rf .installed.cfg downloads/ .mr.developer.cfg parts/ bin/ develop-eggs/ eggs/*egg
fi
touch etc/sys/settings-local.cfg
git checkout etc/project/versions.cfg

