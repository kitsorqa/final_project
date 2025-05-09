# Проект по тестированию онлайн сервиса по подбору и консультации с психологами [ЯСНО](https://yasno.live/)

# Список проверок, реализованных в автотестах:
### UI автотесты:
- Работа фильтров на странице
- Фильтры в модалке
- Футер страницы
- Хедер страницы
- Карточка психолога

### API тесты:
- Получение списка психологов
- Возвращаемое количество психологов
- Пресеты
- Информация по конкретному психологу

# Запуск локально

1. Склонировать проект
```
git clone https://github.com/kitsorqa/final_project.git
```
2. Установить зависимости проекта

```
python -m venv .venv
source .venv/bin/activate
pip3 install -r ./requirements.txt
```

3. Запуск тестов

UI-тесты

```
pytest ./tests/ui_tests
```

API-тесты

```
pytest ./tests/api_tests
```

mobile-тесты

```
pytest ./tests/mobile_tests
```

Если необходимо запустить мобильные тесты на реальном девайса

```
context = 'real_device'
```

Для запуска мобильных тестов на эмуляторе

```
context=emulator
```

4. Генерация отчетности

```
cd ./tests/{Нужная тестовая директория}
allure serve allure-results/
ИЛИ
allure generate -o {название сгенерированного отчета}
allure open {название сгенерированного отчета}
```


# Используемые технологии

<p align="center">
<img src="https://github.com/kitsorqa/final_project/blob/main/imgs/requests.jpg" width="75">
<img src="https://github.com/kitsorqa/final_project/blob/main/imgs/Jenkins.png" width="75">
<img src="https://github.com/kitsorqa/final_project/blob/main/imgs/Pytest_logo.svg.png" width="75">
<img src="https://github.com/kitsorqa/final_project/blob/main/imgs/Python.svg.png" width="75">
<img src="https://github.com/kitsorqa/final_project/blob/main/imgs/allure.png" width="75">
<img src="https://github.com/kitsorqa/final_project/blob/main/imgs/android_studio.jpg" width="75">
<img src="https://github.com/kitsorqa/final_project/blob/main/imgs/appium.png" width="75">
<img src="https://github.com/kitsorqa/final_project/blob/main/imgs/selenium.png" width="75">
<img src="https://github.com/kitsorqa/final_project/blob/main/imgs/selenoid.png" width="75">
