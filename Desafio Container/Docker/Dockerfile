FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        ca-certificates \
        zlib1g-dev \
        libgl1-mesa-dev \
        libx11-dev \
        libxrandr-dev \
        libxinerama-dev \   
        libxcursor-dev \
        libxi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /pbrt

CMD ["/bin/bash"]