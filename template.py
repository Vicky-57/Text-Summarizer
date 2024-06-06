import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="Text_summarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",#components is folder and constructor files (__init__.py) are created inside
    f"src/{project_name}/utilities/__init__.py",
    f"src/{project_name}/utilities/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",#local package setup
    "research/trials.ipynb"#CONTAINS ALL NOTEBOOK EXPERIMENT


]

###LOGIC

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    ##folder creation
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): ##checking size if filesize==0 the file will open
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file:{filepath}") 

    else:
        logging.info(f"{filename} already exists")