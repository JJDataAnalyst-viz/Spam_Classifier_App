#-----------------------###-------------------------------#
############### Template for project ######################
#-----------------------###-------------------------------#

import os 
from pathlib import Path
from typing import List
from src.nlp import logger

logger.info('Hello')
project_name = "nlp"

list_of_files =  [".github/workflows/.gitkeep",
                    f"src/{project_name}/__init__.py",
                    f"src/{project_name}/components/__init__.py",
                    f"src/{project_name}/components/data_ingestion.py",
                    f"src/{project_name}/utils/__init__.py",
                    f"src/{project_name}/utils/common.py",
                    f"src/{project_name}/config/__init__.py",
                    f"src/{project_name}/config/configuration.py",
                    f"src/{project_name}/pipeline/__init__.py",
                    f"src/{project_name}/entity/__init__.py",
                    f"src/{project_name}/entity/config_entity.py",
                    f"src/{project_name}/constants/__init__.py",
                    "config/config.yaml",
                    "params.yaml",
                    "main.py",
                    "Dockerfile",
                    "setup.py",
                    "research/research.ipynb",
                    "app.py"
                ]


def generate_files(list_of_files : List ):
    for files in list_of_files:
        filepath = Path(files)
        filedir,filename = os.path.split(filepath)
        
        if filedir != "":
            os.makedirs(filedir,exist_ok=True)
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):

            with open(filepath,'w') as f:
                pass


if __name__ == "__main__":
    generate_files(list_of_files)

