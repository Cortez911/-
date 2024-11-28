import pytest
import os
import requests

# Здесь мы получаем токен API из переменных окружения.
#  Альтернативно, можно передавать токен через аргументы командной строки pytest:
#  pytest --token <ваш_токен>  test_yougile_api.py

def pytest_addoption(parser):
    parser.addoption(
        "--token", action="store", default=None, help="Yougile API token"
    )


@pytest.fixture(scope="session")
def api_token(request):
    token = request.config.getoption("--token") or os.environ.get("YOYGILE_TOKEN")
    if token is None:
        pytest.fail("Yougile API token is required.  Укажите токен через переменную окружения YOYGILE_TOKEN или опцию командной строки --token")
    return token


@pytest.fixture(scope="session")
def api_client(api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    return requests.Session()
