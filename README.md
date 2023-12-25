<p align="center">
  <img alt="" src="https://imgbb.com/"><img src="https://i.ibb.co/f0c6Z9h/top-secret-small-removebg.png" width="500px">
</p>	

> > HTTP сервис для одноразовых секретов.

### about
Позволяет создать секрет, задать кодовую фразу для его открытия и cгенерировать код, по которому можно прочитать секрет. UI нет, это JSON Api сервис.

- Метод `/generate` принимает секрет и пароль и отдавать `secret_key`по которому этот секрет можно получить.
- Метод `/secrets` принимает на вход кодовую фразу и пароль -> отдает секрет.


<details>
 <summary>Требования</summary>
<ul>
  <li>Язык программирования: Python >=3.7 :heavy_check_mark:</li>
  <li>Использование [Docker](https://www.docker.com/), сервис должен запускаться с помощью `[docker-compose up](https://docs.docker.com/compose/reference/up/)`. :heavy_check_mark:</li>
  <li>Код должен соответствовать PEP, необходимо использование type hints, к публичным методам должна быть написана документация на английском языке. :heavy_check_mark:</li>
</ul>
</details>

***

<details>
 <summary>Усложнения</summary>
<ul>
<li>Написаны тесты (постарайтесь достичь покрытия в 70% и больше). Вы можете использовать [pytest](https://docs.pytest.org/en/latest/) или любую другую библиотеку для тестирования. 💢 </li>
<li>Сервис асинхронно обрабатывает запросы. :heavy_check_mark: </li>
<li>Данные сервиса хранятся во внешнем хранилище, запуск которого также описан в `docker-compose`. Мы рекомендуем использовать [MongoDB](https://www.mongodb.com/), но Вы можете использовать любую подходящую базу. :heavy_check_mark: </li>
<li>Секреты и кодовые фразы не хранятся в базе в открытом виде. :heavy_check_mark: </li>
<li>Добавлена возможность задавать время жизни для секретов. Можно попробовать реализовать это с помощью [TTL индексов](https://docs.mongodb.com/manual/core/index-ttl/). :heavy_check_mark: </li>
</ul>
</details>