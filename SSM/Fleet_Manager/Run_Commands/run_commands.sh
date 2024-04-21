#!/bin/bash
{
    # You can copy for the console only those commands
    uname -a
    echo
    lsb_release -a
    echo
    date
    echo
    ps aux | grep root | cut -d" " -f 1
    echo
    df -h
    echo
    free -h
} > OUTPUT.txt