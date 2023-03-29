#!/usr/bin/env bash

# 用于初始化环境变量的函数，如PATH、PYTHONPATH等
#bin      - PATH
#include  - CPLUS_INCLUDE_PATH、C_INCLUDE_PATH   #c++和c
#lib      - LIBRARY_PATH、LD_LIBRARY_PATH、ClassPATH
#module   - PYTHONPATH
function prepare() {
    echo 'begin prepare'
    day=`date +%Y%m%d`
    sh_log_path="./myapp/logs/sh_${day}.log"
}

function compile() {
    # 方式一：子进程中console输出，只能通过subprocess.PIPE给父进程输出
    echo 'begin compile'
    # 方式二：子进程如果是执行python程序，那么可用logger打印输出到文件中；如果是shell程序，那么可直接输出到文件
    echo 'begin compile' >> ${sh_log_path}
}

function versionset() {
    echo 'begin versionset'
}

function package() {
    echo 'begin package'
}

function release() {
    echo 'begin release'
}

function main() {
    active="$1"
    if [ "$active" == 'compile' ];then
      prepare
      compile
    elif [ "$active" == 'release' ];then
      prepare
      versionset
      package
      release
    else
      echo 'Usage:param like prepare compile versionset package release!'
      exit 1
    fi
}

main $@
exit $?
