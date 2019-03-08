FROM python:3

RUN apt-get update
RUN apt-get install -y --fix-missing \
  #curl \
  #dnsutils \
  #vim \
  net-tools

# get ContainerPilot release
ENV CONTAINERPILOT_VERSION 3.8.0
RUN export checksum=84642c13683ddae6ccb63386e6160e8cb2439c26 \
    && curl -Lso /tmp/containerpilot.tar.gz \
         "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz" \
    && echo "${checksum}  /tmp/containerpilot.tar.gz" | sha1sum -c \
    && tar zxf /tmp/containerpilot.tar.gz -C /usr/local/bin \
    && rm /tmp/containerpilot.tar.gz

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords

# copied this down r/t install problems (to speed re-try)
# RUN apt-get install -y --fix-missing \
#   curl \
#   dnsutils \
#   vim \
#   net-tools

COPY code/ /code/
# add config file
COPY containerpilot.json5 /etc/containerpilot.json5

CMD /usr/local/bin/containerpilot -config /etc/containerpilot.json5