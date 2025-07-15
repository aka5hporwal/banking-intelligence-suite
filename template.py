import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "intelligentBanking"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
    
]

for file_path in list_of_files:
    file_path = Path(file_path)
    try:
        if not file_path.exists():
            if file_path.suffix == '':
                # Create directory
                os.makedirs(file_path, exist_ok=True)
                logging.info(f"Created directory: {file_path}")
            else:
                # Create file
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_path, 'w') as f:
                    pass
                logging.info(f"Created file: {file_path}")
        else:
            logging.info(f"File or directory already exists: {file_path}")
    except Exception as e:
        logging.error(f"Error creating {file_path}: {e}")