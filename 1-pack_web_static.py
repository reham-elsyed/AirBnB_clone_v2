#!/usr/bin/python3
"""
All files in the folder web_static must be added to the final archive
All archives must bein the folder versions
(your function-create this folder if it doesn't exist)
The name
web_static_<year><month><day><hour><minute><second>.tgz
if the archive has been correctly generated

Otherwise, it should return None
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
