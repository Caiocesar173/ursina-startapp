import json
import time
import shutil
from tqdm import tqdm
from pathlib import Path
from termcolor import colored

def create_project_structure(project_name, directory="."):
    script_dir = Path(__file__).resolve().parent
    project_path = Path(directory) / project_name

    tasks = [
        {"desc": "Criando diretórios principais", "func": create_main_dirs, "args": [project_path]},
        {"desc": "Adicionando configuração global", "func": add_global_config, "args": [project_path]},
        {"desc": "Copiando arquivos de recursos", "func": copy_resource_files, "args": [script_dir, project_path]}
    ]

    print(colored(f"Iniciando a instalação do novo app Ursina Engine no diretório {directory}", 'yellow'))

    with tqdm(total=len(tasks), desc=colored("Instalando", 'blue'), ncols=100) as pbar:
        for task in tasks:
            task["func"](*task["args"])
            pbar.update(1)
            time.sleep(0.5)  # Simula algum tempo de processamento

    print(colored("\n[Ursina Engine] App instalado com sucesso!", 'green'))

def create_main_dirs(project_path):
    (project_path / "modules").mkdir(parents=True, exist_ok=True)
    (project_path / "configs").mkdir(exist_ok=True)

def add_global_config(project_path):
    with open(project_path / "configs" / "global_config.json", "w") as f:
        json.dump({"settings": {}}, f, indent=4)

def copy_resource_files(script_dir, project_path):
    shutil.copytree(script_dir.parent / "materials", project_path / "materials")
    shutil.copytree(script_dir.parent / "textures", project_path / "textures")
    shutil.copytree(script_dir.parent / "shaders", project_path / "shaders")
    shutil.copytree(script_dir.parent / "scenes", project_path / "scenes")
    shutil.copy(script_dir.parent / "modules/default_main.py", f"{project_path}/app.py")
    shutil.copy(script_dir.parent / "abstracts/readme_abstract.txt", f"{project_path}/README.md")
    shutil.copy(script_dir.parent / "abstracts/gitignore_abstract.txt", f"{project_path}/.gitignore")
    shutil.copy(script_dir.parent / "abstracts/requirements_abstract.txt", f"{project_path}/requirements.txt")
