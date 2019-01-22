---
author: "Joseph Long"
title: "Using containers to move computations to HPC and the Cloud"
---

Containers allow you to bundle up a program or script and all the packages and libraries it uses in a single archive that runs on any computer with a container runtime like Docker or Singularity (including the University HPC systems).

To follow [the slides](/downloads/2018-19/containers/slides.pdf), you will need to create a DockerHub account and install Docker Desktop for your platform:

- Mac: https://store.docker.com/editions/community/docker-ce-desktop-mac
- Windows: https://store.docker.com/editions/community/docker-ce-desktop-windows
- Linux: consult the Manual for your distribution (e.g. for Ubuntu, https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce )

The full text of the example Dockerfile we built is below:

```
FROM centos:6.10
RUN yum install epel-release -y
RUN yum update -y
RUN rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
RUN rpm -Uvh http://li.nux.ro/download/nux/dextop/el6/x86_64/nux-dextop-release-0-2.el6.nux.noarch.rpm
RUN yum install ffmpeg ffmpeg-devel -y
```

