# PlusMinus
Plus minus site

Для начала нужно установить все библиотеки из venv
Перейти в деректорию firstsite
в консоли виртуального окружение прописать python manage.py runserver [порт]
Открыть в браузере http://127.0.0.1:[порт]/


Для начала работы создать новую ветку, назвать своим ником.
Заливать свой код на ветку и делать pull request
git checkout -b "branch name"

После изменений
git add .
git commit -m "сообщение комиита"
git push -u origin название ветки

Для подключения файлов js, css можно использовать {% static('Fsite/') %}
Для унаследования от базовых шаблонов {% extends('Fsite/') %}
{{}} -- Операции на вывод
{%%} -- Операции для for while if и тд

при работе с формами не забывать использовать {{csrf_token}} -- это поле инпут скрытое от пользователей но при этом защищает от отправки форм за других пользователей

![image](https://user-images.githubusercontent.com/87126594/206483525-bff2303d-2881-4f21-9365-330955e96599.png)
![image](https://user-images.githubusercontent.com/87126594/206483539-6d790ec0-5965-40f0-b060-6d394ac3fa97.png)


Пока все
