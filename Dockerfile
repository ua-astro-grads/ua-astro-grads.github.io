# The FROM instruction initializes a new build stage and sets the Base
# Image for subsequent instructions.  We use the official Debian 9
# (codename Stretch) image here.
FROM debian:stretch

# The base image is minimal with very few software packages.  We
# udpate apt and install python-pip with recommanded packages here.
RUN     apt-get -qq update &&\
        apt-get install -y python-pip &&\
        apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Next, we install astroML's dependencies and astroML itself using pip.
RUN     pip install numpy scipy scikit-learn matplotlib astropy &&\
	pip install astroML astroML_addons

# Change the default work directory to "/root" inside the container.
WORKDIR /root
