import json
import time
import shutil
import uuid
from tqdm import tqdm
from pathlib import Path
from termcolor import colored

def create_project_structure(project_name, directory="."):
    script_dir = Path(__file__).resolve().parent
    project_path = Path(directory) / project_name

    tasks = [
        {"desc": "Criando diretórios principais", "func": create_main_dirs, "args": [project_path]},
        {"desc": "Adicionando configuração global", "func": add_global_config, "args": [project_path]},
        {"desc": "Copiando arquivos de recursos", "func": copy_resource_files, "args": [script_dir, project_path]},
        {"desc": "Gerando dados do editor", "func": create_editor_data, "args": [project_path]}
    ]

    print(colored(f"Iniciando a instalação do novo app Ursina Engine no diretório {directory}", 'yellow'))

    with tqdm(total=len(tasks), desc=colored("Instalando", 'blue'), ncols=100) as pbar:
        for task in tasks:
            task["func"](*task["args"])
            pbar.update(1)
            time.sleep(0.5)  # Simula algum tempo de processamento

    print(colored("\n[Ursina Engine] App instalado com sucesso!", 'green'))

def create_main_dirs(project_path):
    (project_path / "configs").mkdir(parents=True, exist_ok=True)
    (project_path / "prefabs").mkdir(parents=True, exist_ok=True)
    (project_path / "abstracts").mkdir(parents=True, exist_ok=True)
    (project_path / "modules").mkdir(parents=True, exist_ok=True)
    (project_path / "models").mkdir(parents=True, exist_ok=True)

def add_global_config(project_path):
    with open(project_path / "configs" / "global_config.json", "w") as f:
        json.dump({"settings": {}}, f, indent=4)

def copy_resource_files(script_dir, project_path):
    shutil.copytree(script_dir.parent / "materials", project_path / "materials")
    shutil.copytree(script_dir.parent / "textures", project_path / "textures")
    shutil.copytree(script_dir.parent / "shaders", project_path / "shaders")
    shutil.copytree(script_dir.parent / "scenes", project_path / "scenes")

    shutil.copy(script_dir.parent / "modules/default_main.py", f"{project_path}/app.py")

    shutil.copy(script_dir.parent / "abstracts/__init___abstracts_abstract.txt", f"{project_path}/abstracts/__init__.py")
    shutil.copy(script_dir.parent / "abstracts/game_object_abstract.txt", f"{project_path}/abstracts/game_object.py")
    shutil.copy(script_dir.parent / "abstracts/material_abstract.txt", f"{project_path}/abstracts/material.py")
    shutil.copy(script_dir.parent / "abstracts/scene_abstract.txt", f"{project_path}/abstracts/scene.py")

    shutil.copy(script_dir.parent / "abstracts/readme_abstract.txt", f"{project_path}/README.md")
    shutil.copy(script_dir.parent / "abstracts/gitignore_abstract.txt", f"{project_path}/.gitignore")
    shutil.copy(script_dir.parent / "abstracts/requirements_abstract.txt", f"{project_path}/requirements.txt")


def _scan_assets(project_path):
    """Varre pastas do projeto e retorna lista de assets (path relativo, type, source_format)."""
    assets = []
    type_dirs = [
        ("materials", "material", None),
        ("textures", "texture", None),
        ("models", "model", "egg"),
        ("shaders", "shader", None),
        ("scenes", "scene", None),
        ("prefabs", "prefab", None),
    ]
    for dir_name, asset_type, default_fmt in type_dirs:
        d = project_path / dir_name
        if not d.is_dir():
            continue
        for f in d.rglob("*"):
            if f.is_file():
                try:
                    rel = str(f.relative_to(project_path)).replace("\\", "/")
                except ValueError:
                    continue
                suf = f.suffix.lower().lstrip(".")
                fmt = suf if suf in ("egg", "glb", "gltf", "fbx", "blend", "obj", "glsl", "py", "json") else (default_fmt or "")
                assets.append({"path": rel, "type": asset_type, "source_format": fmt or "egg"})
    return assets


def create_editor_data(project_path):
    """Cria configs/editor_state.json com cena alinhada ao Scene + InitialScene: Main Camera, Cube, Player, Floor, Light."""
    project_path = Path(project_path)
    configs = project_path / "configs"
    configs.mkdir(parents=True, exist_ok=True)

    cam_id = str(uuid.uuid4())
    go_id = str(uuid.uuid4())
    player_id = str(uuid.uuid4())
    floor_id = str(uuid.uuid4())
    light_id = str(uuid.uuid4())
    scene = [
        {
            "id": cam_id,
            "name": "Main Camera",
            "parent_id": None,
            "position": [0.0, 0.0, 0.0],
            "rotation": [0.0, 0.0, 0.0],
            "scale": [1.0, 1.0, 1.0],
            "model": "",
            "texture": "",
            "material": "",
            "shader": "shaders/basic_shader",
            "visible": True,
        },
        {
            "id": go_id,
            "name": "Cube",
            "parent_id": None,
            "position": [0.0, 1.0, 0.0],
            "rotation": [0.0, 0.0, 0.0],
            "scale": [1.0, 1.0, 1.0],
            "model": "cube",
            "texture": "",
            "material": "materials/prototype/prototype_orange_material.py",
            "visible": True,
        },
        {
            "id": player_id,
            "name": "Player",
            "parent_id": None,
            "position": [0.0, 2.0, 0.0],
            "rotation": [0.0, 0.0, 0.0],
            "scale": [1.0, 1.0, 1.0],
            "model": "",
            "texture": "",
            "material": "",
            "visible": True,
        },
        {
            "id": floor_id,
            "name": "Floor",
            "parent_id": None,
            "position": [0.0, 0.0, 0.0],
            "rotation": [0.0, 0.0, 0.0],
            "scale": [100.0, 1.0, 100.0],
            "model": "plane",
            "texture": "",
            "material": "materials/prototype/prototype_dark_material.py",
            "visible": True,
        },
        {
            "id": light_id,
            "name": "Light",
            "parent_id": None,
            "position": [0.0, 0.0, 0.0],
            "rotation": [0.0, 0.0, 0.0],
            "scale": [1.0, 1.0, 1.0],
            "model": "",
            "texture": "",
            "material": "",
            "visible": True,
        },
    ]
    assets = _scan_assets(project_path)
    scene_settings = {
        "skybox": False,
        "ambient_light": True,
        "default_shader": "shaders/basic_shader",
    }
    state = {"scene": scene, "assets": assets, "scene_settings": scene_settings}
    out = configs / "editor_state.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
