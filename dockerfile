FROM python:3
WORKDIR /exchangeProject
COPY requirements.txt /exchangeProject/
RUN pip install -r requirements.txt
COPY .env /exchangeProject/
COPY . /exchangeProject/