FROM python:3.7

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV SHELL=/bin/bash

ENV BISBISLIB_RAWDATA_DIR=/home/data/rawdata/01_医療系

ARG USERNAME=${USERNAME}
ARG USER_UID=${USER_UID}
ARG USER_GID=${USER_GID}

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ssh \
    git \
    libopencv-dev

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

COPY ./requirements.txt /tmp/
RUN pip install -U pip && \
    pip --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt

USER $USERNAME

WORKDIR /workspace
