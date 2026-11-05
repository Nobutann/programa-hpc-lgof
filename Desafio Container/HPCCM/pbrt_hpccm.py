from hpccm.building_blocks.packages import packages
from hpccm.primitives.baseimage import baseimage
from hpccm.primitives.workdir import workdir
from hpccm.primitives.raw import raw

Stage0 += baseimage(image="ubuntu:22.04")

Stage0 += packages(apt=[
    "build-essential",
    "cmake",
    "git",
    "ca-certificates",
    "zlib1g-dev",
    "libgl1-mesa-dev",
    "libx11-dev",
    "libxrandr-dev",
    "libxinerama-dev",
    "libxcursor-dev",
    "libxi-dev",
])

Stage0 += workdir(directory="/pbrt")

Stage0 += raw(
    docker='CMD ["/bin/bash"]',
    singularity="""%runscript
    cd /pbrt
    exec /bin/bash "$@"
"""
)