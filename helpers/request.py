import json
import logging
import os

import allure
from utils.attachments import request_with_logs
from jsonschema import validate
from pathlib import Path


def send_request(endpoint, method, data=''):

    allure.step(f'Эндпоинт запроса: {endpoint}')
    if not (data == '' or method == 'get'):
        with open(Path(__file__).parent.parent.joinpath(f'helpers/schemas/request_schemas{endpoint}.json')) as file:
            validate(data, schema=json.loads(file.read()))
    response = request_with_logs(f"{os.getenv("BASE_URL")}/api/v1/public/therapists{endpoint}", method, data)

    with open(Path(__file__).parent.parent.joinpath(f'helpers/schemas/response_schemas{endpoint}.json')) as file:
        validate(response.json(), schema=json.loads(file.read()))

    return response


def check_response_code(response, code):
    allure.step(f'Проверка статуса ответа')
    assert response.status_code == code
