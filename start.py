#!/usr/bin/env python
#coding:utf-8
import os


if __name__ == "__main__":
    host = raw_input("Hosts: ")
    uid = raw_input("uid: ")
    cmd = "erl -pa _build/default/lib/*/ebin -s testc start_link %s %s" % (host, uid)
    os.system(cmd)

