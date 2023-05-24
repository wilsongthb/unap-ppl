FROM python:3.8
RUN python -m venv /opt/venv
COPY requirements.txt .
RUN pip install -r requirements.txt