import os
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    # Se configura la variable de entorno para indicar el ambiente de prueba
    os.environ['TEST_ENV'] = 'development'
    # Se realizan acciones para inicializar el ambiente, por ejemplo, iniciar una base de datos o un servidor web
    # ...
    yield
    # Se realizan acciones para limpiar el ambiente después de la ejecución de las pruebas, por ejemplo, eliminar la
    # base de datos o detener el servidor web
