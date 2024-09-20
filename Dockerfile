FROM python:3.10
WORKDIR /alibaba
COPY requirements.txt /alibaba/
RUN pip install -r requirements.txt
COPY . /alibaba/
EXPOSE 8001
CMD ["python manage.py migrate && python manage.py runserver"]