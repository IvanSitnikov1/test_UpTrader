#### Тестовое задание UpTrader

#### Описание проекта:
Реализован django app, представляющий древовидное меню.  
1) Меню реализовано через template tag.
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django.
5) Активный пункт меню определяется исходя из URL текущей страницы.
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД.

### Запуск проекта:
Запуск проекта возможен через докер:  
 - docker build -t tree_menu .  
 - docker run -p 8000:8000 tree_menu  

Либо стандартными средствами django:  
- установка зависимостей из requirements.txt  
- django manage.py runserver

Проект доступен по адресу:  
http://127.0.0.1:8000/

#### Тестирование:
Доступ к админ панели:  
http://127.0.0.1:8000/admin/  
База данных заполнена тестовыми данными, а так же создан тестовый суперпользователь:  
username: admin  
password: admin