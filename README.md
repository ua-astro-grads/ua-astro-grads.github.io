How-to Docker (with astroML)
============================

This is a minimal Docker tutorial using astroML as an example.  Docker
is needed in order to try it out.  The Docker Community Edition (CE)
is free and is avliable at the [Docker Website](https://www.docker.com/get-docker).
It supports all the major platforms from Linux (e.g.,
[Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)), to
[Mac OS X](https://store.docker.com/editions/community/docker-ce-desktop-mac), and even
[Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows).

`Dockerfile` is the main part of this tutorial.  It tells Docker how
to create a Docker image, which you can instanceize it into Docker
containers on any machine with Docker---from your laptop to a powerful
many-core virtual machine (VM) on CyVerse, to thousands of VMs that
you launch with container orchestration platforms on Google Cloud
Platform.

`Makefile` contains the commands that we will run during the tutorial.

`plot_spectrum_sum_of_norms.py` is an example from astroML.  It is
modified to run better in a container environment.
