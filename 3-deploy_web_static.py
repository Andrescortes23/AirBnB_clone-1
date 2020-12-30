#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from contents of web_static"""
from time import strftime
from datetime import date
from fabric.api import local, env, run, put
from os import path


env.hosts = ['35.237.92.39', '35.231.86.111']
env.user = 'ubuntu'


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

    if path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            file_path = archive_path.split('/')[-1]
            the_file = file_path.replace(".tgz", "")
            run("sudo mkdir -p /data/web_static/releases/{}".format
                (the_file))
            run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}".format
                (file_path, the_file))
            run("sudo rm -f /tmp/{}".format(the_file))
            run("sudo mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(the_file, the_file))
            run("sudo rm -rf /data/web_static/releases/{}/web_static"
                .format(the_file))
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s /data/web_static/releases/{}\
            /data/web_static/current".format(the_file))
            return True
        except:
            return False
    else:
        return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    Trufal = do_deploy(archive_path)
    return Trufal
