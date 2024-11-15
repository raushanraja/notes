FROM raushanraja/jammybase:latest
ENV PULSE_SERVER=host.docker.internal
ARG SIPP_VERSION="3.6.1"


RUN apt install -y 
RUN apt update

RUN apt-get install -y cmake libncurses5-dev libssl-dev libsctp-dev libpcap-dev wget openssl ffmpeg python3-pip debhelper  python3 dh-python python3-all-dev cython3 libasound2-dev libssl-dev libv4l-dev libavcodec-dev libavformat-dev libopencore-amrnb-dev libopencore-amrwb-dev libavutil-dev libswscale-dev libx264-dev libvpx-dev libopus-dev libsqlite3-dev pkg-config uuid-dev pulseaudio alsa-utils sox libsox-fmt-all

RUN pip3 install  pyopenssl service_identity dnspython twisted==22.10.0 cython python-dateutil greenlet==2.0.0 gmpy2 zope lxml gevent==22.10.2
RUN apt-get install -y  cython3 git

WORKDIR /usr/src
RUN git clone https://github.com/AGProjects/python3-eventlib.git
WORKDIR /usr/src/python3-eventlib
RUN python3 setup.py install

WORKDIR /usr/src
RUN git clone https://github.com/AGProjects/python3-xcaplib.git
WORKDIR /usr/src/python3-xcaplib
RUN python3 setup.py install

WORKDIR /usr/src
RUN git clone https://github.com/AGProjects/python3-msrplib.git
WORKDIR /usr/src/python3-msrplib
RUN python3 setup.py install

WORKDIR /usr/src
RUN git clone https://github.com/AGProjects/python3-gnutls.git
WORKDIR /usr/src/python3-gnutls
RUN python3 setup.py install

WORKDIR /usr/src
RUN git clone https://github.com/AGProjects/python3-application.git
WORKDIR /usr/src/python3-application
RUN python3 setup.py install


WORKDIR /usr/src
RUN git clone  https://github.com/AGProjects/python3-otr.git
WORKDIR /usr/src/python3-otr
RUN python3 setup.py install

WORKDIR /usr/src
RUN git clone https://github.com/AGProjects/python3-sipsimple.git
WORKDIR /usr/src/python3-sipsimple
RUN chmod +x get_dependencies.sh && ./get_dependencies.sh && python3 setup.py install

WORKDIR /usr/src
RUN git clone https://github.com/AGProjects/sipclients3.git
RUN cd sipclients3 && pip3 install -r requirements.txt && python3 setup.py install

WORKDIR /usr/src
RUN wget --no-check-certificate "https://github.com/SIPp/sipp/releases/download/v$SIPP_VERSION/sipp-$SIPP_VERSION.tar.gz" && \
    tar -xzf sipp-$SIPP_VERSION.tar.gz -C . && \
    cd sipp-$SIPP_VERSION && \
    ./build.sh --full && cp sipp /usr/local/bin

WORKDIR /usr/app
CMD ["tail", "-f", "/dev/null"]
