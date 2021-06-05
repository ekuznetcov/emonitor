# Средство визуализации данных параллельных программ EMonitor
Подробнее в [Wiki](https://github.com/ekuznetcov/emonitor/tree/master/Wiki)

### Структура проекта
#### Внутренняя структура:
* Парсер .messtat файлов(api)
* Пользовательский интерфейс(frontend)
* Обратный прокси-сервер(nginx)

###  Локальная работа с проектом

В условиях, когда приложение разворачивается локально папка /home/user/energy пробрасывается в контейнер api в нее можно положить папку с результатами работы программы messtat, также эти файлы можно будет загрузить через интерфейс веб-приложения.

```shell
# Запуск приложений в Docker Compose
docker-compose up -d --build

# Завершение работы
docker-compose down
```

###  Запуск на production-сервере
```shell
# Запуск приложений в Docker Compose
docker-compose up -d --build

# Завершение работы
docker-compose down
```
### Развертывание без подключения к интернету
В условиях, когда систему необходимо развернуть в закрытой подсети, необходимо
собрать образы приложения на машине с подключением к сети , после чего скопировать полученные данные на машину
