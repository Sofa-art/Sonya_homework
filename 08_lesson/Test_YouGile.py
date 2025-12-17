import pytest
import requests

base_url="https://ru.yougile.com/api-v2/"
token="token"
key=token

# Получение ключа
def test_company():
        credits= {
  "login": "login",
  "password": "password",
  "companyId":""
}
        resp=requests.post(base_url+'auth/keys/get', json=credits)
        response_data = resp.json()
        return response_data[0]['key']


# Добавить компанию:
def test_create_project_positive():
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
        }
        project = {
            "title": "SkyPro"
        }
        resp = requests.post(base_url + 'projects',
                             headers=headers,
                             json=project)
        return resp.json()

# Добавление компании с пустым названием
def test_create_project_negative():
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
        }
        project = {
            "title": ""
        }
        resp = requests.post(base_url + 'projects',
                             headers=headers,
                             json=project)
        return resp.json()

# Получить проект по id
def test_get_project_with_id_positive():
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(base_url + f'projects/{"project_id"}',
                            headers=headers)
        return resp

# Получение по неправильному id
def test_get_project_with_id_negative():
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(base_url + f'projects/{"123456789"}',
                            headers=headers)
        return resp

    

 # Изменить проект
def test_edit_project_positive():
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
        }
        project = {
            "title": "SkyPro_New"   
        }
        resp = requests.put(base_url + f'projects/{"project_id"}',
                            headers=headers, json=project)
        return resp.json()

# Изменить проект с неправильным id
def test_edit_project_negative():
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
        }
        project = {
            "title": "SkyPro_New"   
        }
        resp = requests.put(base_url + f'projects/{"0e75487b-e1b8-4f0e-8c5c"}',
                            headers=headers, json=project)
        return resp.json()
   
     
   
   

    





        

  


    
    

