FROM ubuntu

RUN apt-get update
RUN apt-get install tzdata

RUN apt-get install -y python3 \
    python3-pip \
    x11-apps \
    firefox 

RUN useradd -ms /bin/bash user
WORKDIR /selenium
ADD . /selenium
RUN mkdir /selenium/logs

RUN pip3 install -r requirements.txt

RUN chown -R user:user /selenium
RUN chmod 755 /selenium

USER user
RUN cd /selenium/data

CMD ["./error.py"]
ENTRYPOINT ["python3"]