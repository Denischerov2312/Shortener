# Обрезка ссылок с помощью Битли

  

Bitly URL shortener - консольная программа, которая используется для укорачивания ссылок и получения количество кликов по ним.

  

### Как установить


На сайте [Bitly.com](https://app.bitly.com/settings/api/) вы должны получить API-токен. `GENERIC ACCES TOKEN` - нужный тип токена.

  

API-токен надо положить в виртуальную среду, в переменную под названием `API_BITLY_TOKEN`.

  

Запускается программа в консоле, командой `python main.py *your_link*`.

Выглядит это примерно так:

```console

$ python main.py https://www.google.ru/
https://bit.ly/3pKSxHl

```

  

Python3 должен быть уже установлен.

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```

pip install -r requirements.txt

```

  

### Цель проекта

  

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).