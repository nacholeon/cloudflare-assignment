{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fmodern\fcharset0 CourierNewPS-BoldMT;\f1\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;\red21\green168\blue175;\red26\green26\blue26;\red255\green255\blue255;
\red23\green177\blue17;\red64\green140\blue9;\red96\green140\blue196;}
{\*\expandedcolortbl;;\cssrgb\c0\c70980\c74118;\cssrgb\c13333\c13333\c13333;\cssrgb\c100000\c100000\c100000;
\cssrgb\c0\c72941\c7451;\cssrgb\c30588\c60392\c2353;\cssrgb\c44706\c62353\c81176;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl300\partightenfactor0

\f0\b\fs26 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  flask 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 import 
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 Flask, request\
\
app = Flask(__name__)\
\
@app.route(
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 '/'
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 )\AppleTypeServices\AppleTypeServicesF65539 \cb6  \AppleTypeServices\AppleTypeServicesF65539 \cb3 \
\

\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 def\AppleTypeServices\AppleTypeServicesF65539 \cf7 \strokec7  index
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 ():\
   headers = request.headers\
   
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 return \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 "Request headers:\\n" 
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 + str(headers)\
\
\

\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 if
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  __name__ == 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 '__main__'
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 :\AppleTypeServices\AppleTypeServicesF65539 \cb6  \AppleTypeServices\AppleTypeServicesF65539 \cb3 \
    app.run()\
}