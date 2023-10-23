# Network Security
----------------------------
## A company with an online service that provides clear identification of changing traffic has a specialized security department that filters and analyzes this traffic. For him, a model was built for determining the type of traffic.

### During the work, all the main stages of the study were carried out:
- downloading and reviewing data,

- Preliminary processing,

- selection of the final set of training indicators,

- selection and training of the model,

- final assessment of the quality of prediction of the best models


## Инструкция по сборке и запуску:

Этот репозиторий содержит код для создания сервера, использующего модель CatBoost для предсказания. Ниже приведены инструкции по сборке и запуску сервера, а также проверки работы модели.

### Шаг 1: Установка зависимостей

Убедитесь, что у вас установлен Docker. [Инструкции по установке Docker](https://docs.docker.com/get-docker/)

### Шаг 2: Сборка и запуск Docker-контейнера

docker build -t default-service:v01 .
docker run -it --rm -p 8989:8989 default-service:v01

### Шаг 3: Отправка запроса и проверка предсказаний

Вы можете использовать любой инструмент для отправки POST-запросов. В примере я использую JSON. В файле 'test' содержится тестовый запрос с помощью которого можно проверить работу модели

### Примечание
Если у вас возникли какие-то проблемы с сборкой или запуском сервера, пожалуйста, обратитесь к документации Docker.
Также, убедитесь, что все файлы (включая `loan_dtm_model.cbm`, `main.py`, `requirements.txt` и `Dockerfile`) находятся в корневой директории вашего репозитория на GitHub перед тем как следовать этим инструкциям.

