import requests
import pytest

class YougileAPI:
    def __init__(self, api_token, base_url="https://ru.yougile.com/api-v2"):
        self.api_client = requests.Session()
        self.api_client.headers.update({'Authorization': f'Bearer {api_token}'})
        self.base_url = base_url

    def create_project(self, data):
        response = self.api_client.post(f"{self.base_url}/projects", json=data)
        return response

    def get_projects(self):
        response = self.api_client.get(f"{self.base_url}/projects")
        return response

    def update_project(self, project_id, data):
        response = self.api_client.put(f"{self.base_url}/projects/{project_id}", json=data)
        return response

    def delete_project(self, project_id):
        response = self.api_client.delete(f"{self.base_url}/projects/{project_id}")
        return response

    def get_project(self, project_id):
        response = self.api_client.get(f"{self.base_url}/projects/{project_id}")
        return response


@pytest.fixture
def api_client():
    api_token = "токен"  # <--- СЮДА ТОКЕН!
    return YougileAPI(api_token)


def test_create_project_positive(api_client):
    data = {"title": "Test Project"}  # <--- Убрано поле description
    response = api_client.create_project(data)
    assert response.status_code == 201, f"Ошибка при создании проекта: {response.text}"
    project_id = response.json()['id']
    api_client.delete_project(project_id)


def test_create_project_negative(api_client):
    data = {"description": "Missing title"} 
    response = api_client.create_project(data)
    assert response.status_code == 400, f"Ожидалась ошибка 400, но получен код {response.status_code}: {response.text}"


def test_get_projects(api_client):
    response = api_client.get_projects()
    assert response.status_code == 200, f"Ошибка при получении списка проектов: {response.text}"
    data = response.json()
    assert isinstance(data, dict), "Неверный формат ответа"
    assert 'content' in data, "Отсутствует ключ 'content'"
    assert isinstance(data['content'], list), " 'content' не является списком"


def test_update_project(api_client):
    data = {"title": "Test Project"}  # <--- Убрано поле description
    response_create = api_client.create_project(data)
    assert response_create.status_code == 201, f"Ошибка при создании проекта: {response_create.text}"
    project_id = response_create.json()['id']

    new_data = {"title": "Updated Test Project"}  # <--- Убрано поле description
    response_update = api_client.update_project(project_id, new_data)
    assert response_update.status_code == 200, f"Ошибка при обновлении проекта: {response_update.text}"

    response_get = api_client.get_project(project_id)
    assert response_get.status_code == 200, f"Ошибка при получении проекта: {response_get.text}"
    assert response_get.json()['title'] == "Updated Test Project", "Имя проекта не обновлено"

    api_client.delete_project(project_id)


def test_get_project(api_client):
    response = api_client.get_projects()
    if response.status_code == 200:
        projects = response.json()['content']
        if projects:
            project_id = projects[0]['id']
            response = api_client.get_project(project_id)
            assert response.status_code == 200, f"Ошибка при получении проекта: {response.text}"
    else:
        pytest.skip("No projects found")
