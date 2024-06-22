import requests
import json
import os
from .library import Jamworks

class Jamworks_Login:
    """
   
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "token": ("STRING",{"multiline":False,}),
                "user": ("STRING",{"multiline":False,}),
                "password": ("STRING",{"multiline":False,}),
                "JW2_CORE_URL": ("STRING",{"multiline":False,}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("token",)

    FUNCTION = "login"

    CATEGORY = "Jamworks"

    def login(self, token,user, password,JW2_CORE_URL):
        jam = Jamworks(JW2_CORE_URL,"")
        jam.auth(user,password)
        return (jam.token,)

class Jamworks_Download:
    """
   
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "token": ("STRING",{"multiline":False,}),
                "node_id": ("INT",{"display":"number"}),
                "download_path": ("STRING",{"multiline":False,}),
                 "JW2_CONTENT_URL": ("STRING",{"multiline":False,}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_path",)

    FUNCTION = "download"

    CATEGORY = "Jamworks"

    def download(self, token,node_id,download_path,JW2_CONTENT_URL):
        jam = Jamworks("",JW2_CONTENT_URL)
        jam.token = token
        file = jam.getContentsFileInfo(node_id)
        if (file.type!='folder'):
            jam.contentsDownloadFile(node_id,download_path+"/"+file.name)
        else:
            list = jam.contentsList(node_id)
            for e in list['entries']:
                if (e['type']=='file'):
                    jam.contentsDownloadFile(e['node_id'],download_path+"/"+e['name'])

        print([file.name,file.type])
        return (download_path,)


class Shell_Command:
    """
   
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "command": ("STRING",{"multiline":False,}),
                "params": ("STRING",{"multiline":True,}),
            },
        }

    RETURN_TYPES = ("INT","STRING","STRING","STRING")
    RETURN_NAMES = ("RETURN_CODE","STD_OUT","STD_ERR","COMMAND")

    FUNCTION = "run"

    CATEGORY = "Jamworks"

    def run(self, command,params):
        import subprocess
        args = params.split("\n")
        cmd = []
        cmd.append(command)
        for a in args:
            ar = a.split(":")
            for p in ar:
                cmd.append(p)
        com = " ".join(cmd)

        s = subprocess.run(com,capture_output=True,shell=True)
        print(s.returncode)
        return (s.returncode,s.stdout,s.stderr,com)

NODE_DISPLAY_NAME_MAPPINGS = {
    "Jamworks Login": "Logs into Jamworks to obtain a valid user token",
    "Jamworks Download" : "Download a single file or a list of files from Content",
    "Shell Command": "Executes commands with params"
}

