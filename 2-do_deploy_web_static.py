#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from contents of web_static"""
from time import strftime
from datetime import date
from fabric.api import local
env.hosts = ['35.237.92.39', '35.231.86.111']


def do_pack():
    """
    To geberate a tgz
    """

    local("mkdir -p versions")
    tmt = strftime("%Y%m%d%H%M%S")
    creat = local("tar -cvzf versions/web_static_{}.tgz web_static"
                  .format(tmt))
    if creat.succeeded:
        return "versions/web_static_{}.tgz".format(tmt)
    else:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to your web servers, using the function do_deploy
    """

    if archive_path:
        put(archive_path, "/tmp/")
        run("tar xvzf archive_path -C /data/web_static/releases/web_static")
        with cd('/tmp/'):
            sudo('rm -f archive_path')
        with cd('/data/web_static/'):
            sudo('rm -f current')
        run("ln -s /data/web_static/releases/web_static /data/web_static\
        /current")
        return True
    else:
        return False
