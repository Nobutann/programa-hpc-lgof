FROM ubuntu:22.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        cmake \
        git \
        libgl1-mesa-dev \
        libx11-dev \
        libxcursor-dev \
        libxi-dev \
        libxinerama-dev \
        libxrandr-dev \
        zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /pbrt

CMD ["/bin/bash"]


