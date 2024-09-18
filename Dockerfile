# ANCHOR DOCKER COMPOSE
FROM python:3.10.12
# FROM python:3.7.4-alpine3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "taskproject.wsgi:application"]

###################################

# ANCHOR DOCKER GUNICORN
# FROM python:3.10.12
# FROM python:3.7.4-alpine3.10
# ADD taskproject/requirements.txt /app/requirements.txt
# RUN set -ex \
#     && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
#     && python -m venv /env \
#     && /env/bin/pip install --upgrade pip \
#     && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
#     && runDeps="$(scanelf --needed --nobanner --recursive /env \
#         | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
#         | sort -u \
#         | xargs -r apk info --installed \
#         | sort -u)" \
#     && apk add --virtual rundeps $runDeps \
#     && apk del .build-deps

# WORKDIR /app
# COPY . /app
# ENV VIRTUAL_ENV /env
# ENV PATH /env/bin:$PATH
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "taskproject.wsgi:application"]