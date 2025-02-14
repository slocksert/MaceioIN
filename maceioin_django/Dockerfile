FROM python:3.12.3

WORKDIR /code

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x wait-for-it.sh  

EXPOSE 8080

CMD ["sh", "-c", "./wait-for-it.sh mysql_db:3306 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]
