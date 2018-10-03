---
author: "CK Chan"
title: "How-to Docker (with astroML)"
---


**[Slides (PDF)](/downloads/2017-18/chan-cloud-resources.pdf)**

This is a minimal Docker tutorial using astroML as an example.  Docker
is needed in order to try it out.  The Docker Community Edition (CE)
is free and is avliable at the [Docker Website](https://www.docker.com/get-docker).
It supports all the major platforms from Linux (e.g.,
[Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)), to
[Mac OS X](https://store.docker.com/editions/community/docker-ce-desktop-mac), and even
[Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows).

The supporting files for this tutorial are available in the repository for this site under
[downloads/2017-18/chan-howto-docker-astroML](https://github.com/ua-astro-grads/ua-astro-grads.github.io/tree/master/downloads/2017-18/chan-howto-docker-astroML).

[`Dockerfile`](https://github.com/ua-astro-grads/ua-astro-grads.github.io/blob/master/downloads/2017-18/chan-howto-docker-astroML/Dockerfile) is the main part of this tutorial.  It tells Docker how
to create a Docker image, which you can instanceize it into Docker
containers on any machine with Docker---from your laptop to a powerful
many-core virtual machine (VM) on CyVerse, to thousands of VMs that
you launch with container orchestration platforms on Google Cloud
Platform.

[`Makefile`](https://github.com/ua-astro-grads/ua-astro-grads.github.io/blob/master/downloads/2017-18/chan-howto-docker-astroML/Makefile) contains the commands that we will run during the tutorial.

[`plot_spectrum_sum_of_norms.py`](https://github.com/ua-astro-grads/ua-astro-grads.github.io/blob/master/downloads/2017-18/chan-howto-docker-astroML/plot_spectrum_sum_of_norms.py) is an example from astroML.  It is
modified to run better in a container environment.
