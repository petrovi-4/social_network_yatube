<h1>Проект API для YaTube</h1>

<h3>Описание</h3>

API для YaTube представляет собой проект социальной сети в которой релизованы возможности публиковать записи, комментировать записи и реализована возможность подписатьс или отписаться от авторов.

<h3>Запуск проекта</h3>

- Клонировать репозиторий и перейти в него в командной строке.
<p><pre>git clone https://github.com/petrovi-4/api_final_yatube.git</pre></p>

- Установить и активировать виртуальное окружение *(версия Python не ниже 3.7)*:
<p><pre>python3 -m venv venv</pre></p>
<p><pre>sourse venv/bin/activate</pre></p>

- Установить зависимости из файла **requirements.txt**:
<p><pre>python3 -m pip install --upgrade pip</pre></p>
<p><pre>pip install -r requirements.txt</pre></p>

- Выполнить миграции:
<p><pre>python manage.py migrate</pre></p>

- Создаём суперпользователя:
<p><pre>python manage.py createseperuser</pre></p>

- Запускаем проект:
<p><pre>pyhton manage.py runserver</pre></p>

<h3>Примеры работы с API для всех пользователей</h3>

Для неавторизованных пользователей раюота с API доступна в режиме чтения, что-то изменить, создать, подписаться на авторов не получится.
<p><pre>GET /api/v1/posts/ - получить список всех постов.</p>
<p>`GET /api/v1/posts/{id}/` - получение публикации по id.</p>
<p>`GET /api/v1/groups/` - получение списка доступных групп.</p>
<p>`GET /api/v1/groups/{id}/` - получение информации о группе по id.</p>
<p>`GET /api/v1/{post_id}/comments/` - получение всех комментариев поста.</p>
<p>`GET /api/v1/{post_id}/cpmments/{id}/` - получение комментария к посту по id</pre></p>

<h3>Примеры работы с API для авторизованных пользователей</h3>

Для создания поста используем:
<p><pre>POST /api/v1/posts/</pre></p>
Обновление поста:
<p><pre>PUT /api/v1/posts/{id}/</pre></p>
Частичное обновление поста:
<p><pre>PATCH /api/v1/posts/{id}/</pre></p>
Удаление поста:
<p><pre>DEL /api/v1/posts/{id}/</pre></p>
Получение доступа к эндпоинту /api/v1/follow/ доступен только авторизированным пользователям.
<p><pre>GET /api/v1/follow/ - подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса.</pre></p>

- Авторизированные пользователя могут создавать посты, комментировать посты и подписываться на других пользователей.
- Пользователи могут изменять и удалять контент, автором которого они являются.

<h4>Добавлять группу в проект нужно через админ панель Django:</h4>

<pre>admin/</pre> - после авторизации, переходим в раздел Groups и создаём группы

Доступ авторизированным пользователям доступен по JWT токену, который можно получить:
<p><pre>POST /api/v1/jwt/create/</pre></p>
Передав в body данные пользователя:
    <pre>
    {
    "username": "string", 
    "password": "string"
    }</pre>
Полученный токен добавляем в headers [Postman](https://www.postman.com/downloads/), после будут доступны все функции проекта:
<pre>Authorization: Bearer {your_token}</pre>
Обновить JWT-токен:
<pre>POST /api/v1/jwt/refresh/</pre>
В проекте API реализована пагинация (LimitOffsetPagination):
<pre>GET /api/v1/posts/?limit=5&offset=0 - пагинация на 5 постов, начиная с первого</pre>


<h5>Автор:</h5> [Мартынов Сергей](https://github.com/petrovi-4) 

![GitHub User's stars](https://img.shields.io/github/stars/petrovi-4?label=Stars&style=social)</p>
![licence](https://img.shields.io/badge/licence-GPL--3.0-green)</p>
