FROM python:3.7
MAINTAINER Rachael Tordoff

RUN pip3 -q install gunicorn==19.9.0 eventlet==0.24.1
RUN apt-get install -y libpq-dev

COPY / /opt/


RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN tar xvJf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN cp wkhtmltox/bin/wkhtmlto* /usr/bin/
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install -q -r /opt/requirements.txt
EXPOSE 8000

WORKDIR /opt

CMD ["/usr/local/bin/gunicorn", "-k", "eventlet", "--pythonpath", "/opt", "--access-logfile", "-", "manage:manager.app", "--reload", "-b", "0.0.0.0:8000"]
