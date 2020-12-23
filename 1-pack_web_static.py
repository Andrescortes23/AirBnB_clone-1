#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from contents of web_static"""
from time import strftime
from datetime import date
from fabric.api import local


def do_pack():
    """
    To geberate a tgz
    """
    local("mkdir -p versions")
    tmt = strftime("%Y%m%d%H%M%S")
    creat = local("tar -cvzf versions/web_static_{}.tgz web-static"
                  .format(tmt))
    if creat.succeeded:
        return "versions/web_static_{}.tgz".format(tmt)
    else:
        return None
