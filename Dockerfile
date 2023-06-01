FROM openjdk:8-jdk

ARG MODEL_NAME
ARG NETLOGO_VERSION
ARG NETLOGO_NAME=NetLogo-$NETLOGO_VERSION
ARG NETLOGO_URL=https://ccl.northwestern.edu/netlogo/$NETLOGO_VERSION/$NETLOGO_NAME-64.tgz

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    DISPLAY=:14
    
RUN mkdir /home/netlogo \
 && wget $NETLOGO_URL \
 && tar xzf $NETLOGO_NAME-64.tgz -C /home/netlogo --strip-components=1 \
 && rm $NETLOGO_NAME-64.tgz \
 && cp /home/netlogo/netlogo-headless.sh /home/netlogo/netlogo-headw.sh \
 && sed -i -e 's/org.nlogo.headless.Main/org.nlogo.app.App/g' /home/netlogo/netlogo-headw.sh \
 && apt-get update && apt-get install -y libxrender1 libxtst6
    
COPY . /home/

RUN mv /home/src/$MODEL_NAME /home/src/NLModel.nlogo

CMD ["/home/netlogo/netlogo-headw.sh", "/home/src/NLModel.nlogo"]