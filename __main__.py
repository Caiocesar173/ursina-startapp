import argparse
from modules.project_structure import create_project_structure


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crie a estrutura básica para um projeto Ursina.")
    parser.add_argument("project_name", help="O nome do projeto")
    parser.add_argument("--directory", "-d", help="O diretório onde criar o projeto", default=".")
    args = parser.parse_args()

    create_project_structure(args.project_name, args.directory)
