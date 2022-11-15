FROM python:alpine

COPY . app/
WORKDIR app/

RUN pip3 install --upgrade && pip pip3 install bs4 requests pyTelegramBotAPI

CMD ["python3", "app/main.py"]
