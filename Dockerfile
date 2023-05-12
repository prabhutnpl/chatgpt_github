FROM registry.access.redhat.com/ubi8/python-38:1-125.1683014507
user root
RUN mkdir /app
ADD ./main.py /app
ADD ./requirements.txt /app
ADD ./templates /app/templates
WORKDIR /app
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
expose 5000
CMD ["python", "main.py"]