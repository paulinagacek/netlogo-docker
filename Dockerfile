FROM opensciencegrid/osgvo-ubuntu-20.04

ARG MODEL_FOLDER
ARG NETLOGO_VERSION=6.3.0
ARG NETLOGO_HOME=/opt/netlogo
ARG NETLOGO_NAME=NetLogo-$NETLOGO_VERSION

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    NETLOGO_TARBALL=NetLogo-$NETLOGO_VERSION-64.tgz

ENV NETLOGO_URL=https://ccl.northwestern.edu/netlogo/$NETLOGO_VERSION/$NETLOGO_TARBALL

WORKDIR /opt

RUN wget -q $NETLOGO_URL && tar xzf $NETLOGO_TARBALL && ln -sf "NetLogo $NETLOGO_VERSION" netlogo && rm -f $NETLOGO_TARBALL

COPY models /opt/models

RUN mv /opt/models/$MODEL_FOLDER/model.nlogo /opt/models/NLModel.nlogo
RUN mv /opt/models/$MODEL_FOLDER/experiment.xml /opt/models/experiment.xml
RUN mv /opt/models/$MODEL_FOLDER/input.csv /opt/models/input.csv

CMD "./NetLogo 6.3.0/NetLogo_Console" --headless \
--model /opt/models/NLModel.nlogo \
--setup-file /opt/models/experiment.xml \
--table models/table-output.csv \
--spreadsheet models/table-output.csv