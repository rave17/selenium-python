import os
import json
from dotenv import load_dotenv

# Es importante tener en cuenta que las variables de entorno que se utilizan en este archivo deben definirse en un
# archivo .env que se encuentre en la misma carpeta que el archivo read_config.py.

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la ruta del archivo config.json desde una variable de entorno
CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
USERTEST_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'data_test.json')


def get_browser():
    with open(CONFIG_FILE_PATH, "r") as f:
        data = json.load(f)

    for seccion, seccion_valores in data.items():
        print(f'Seccion: {seccion}')
        for clave, valor in seccion_valores.items():
            if isinstance(valor, dict):
                print(f'\t{clave}:')
                for subclave, subvalor in valor.items():
                    print(f'\t\t{subclave}: {subvalor}')
            else:
                print(f'\t{clave}: {valor}')

    print(data)
    return data


def get_url():
    with open(CONFIG_FILE_PATH, "r") as f:
        data = json.load(f)
        print(data['urls']["login"])
        return data['urls']["login"]


def get_users_test():
    with open(USERTEST_FILE_PATH, "r") as f:
        data_test = json.load(f)
        valid_users_data = data_test['users']['valid_users']
        invalid_users_data = data_test['users']['invalid_users']
        print(valid_users_data + invalid_users_data)
        return data_test['users']
