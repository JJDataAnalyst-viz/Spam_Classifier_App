FROM apache/airflow:2.5.1
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir  -r /requirements.txt