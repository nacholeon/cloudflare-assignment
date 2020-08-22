{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;\red26\green26\blue26;\red19\green135\blue136;
}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;\cssrgb\c13333\c13333\c13333;\cssrgb\c2353\c59608\c60392;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl300\partightenfactor0

\f0\fs26 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 FROM debian:latest\
\
RUN apt-get -yqq update\
COPY . /opt/flaskapp\
WORKDIR /opt/flaskapp\
\
\pard\pardeftab720\sl300\partightenfactor0
\AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 # Supervisord\AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 \
\
RUN apt-get install -y supervisor/stable\
RUN mkdir -p /var/log/supervisor\
RUN mkdir -p /etc/supervisor/conf.d/\
COPY supervisord.conf /etc/supervisord.conf\
\
\AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 # Cloudflared\AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 \
\
RUN apt-get install -y wget\
RUN wget -O- {\field{\*\fldinst{HYPERLINK "https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz"}}{\fldrslt https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz}} | tar xz\
RUN mkdir -p /etc/cloudflared/\
COPY cert.pem /etc/cloudflared/\
COPY config.yaml /etc/cloudflared/\
\
\AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 # Python and Flask\AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 \
\
RUN apt-get -yqq install python3 python3-pip\
RUN pip3 install flask\
\
\AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 # Main\AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 \
\
CMD ["/usr/bin/supervisord"]\
\
\
}