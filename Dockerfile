# Establecer el secreto `MODE = apache` en la configuracion de Hugging Face para descargar la base del proyecto
FROM debian:13.4

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-django \
    python3-mysqldb \
    apache2 \
    zip  \
    p7zip-full \
    && rm -rf  /var/lib/apt/lists/*

RUN mkdir djangotutorial
RUN django-admin startproject mysite djangotutorial

RUN apt update 
RUN apt install -y python3-psycopg 
WORKDIR /app/djangotutorial
RUN python3 manage.py startapp polls

# Copia tus archivos modificados encima del proyecto generado
# Los archivos de `proyecto_limpio.zip` deben estar ubicados en esta carpeta
COPY ./djangotutorial/ /app/djangotutorial/

# Prepara comprimidos descargables
RUN cd /app && \
    zip -r /var/www/html/proyecto_limpio.zip djangotutorial; \
    zip -r /var/www/html/polls.zip djangotutorial/polls

EXPOSE 7860

CMD sh -c ' \
    if [ "$MODE" = "apache" ]; then \
        sed -i "s/Listen 80/Listen 7860/" /etc/apache2/ports.conf && \
        sed -i "s/<VirtualHost \\*:80>/<VirtualHost *:7860>/" /etc/apache2/sites-available/000-default.conf && \
        rm -rf /var/www/html/index.html && \
        apachectl -D FOREGROUND; \
    else \
        cd /app/djangotutorial && \
        python3 manage.py makemigrations && \
        python3 manage.py migrate && \
        python3 manage.py runserver 0.0.0.0:7860; \
    fi