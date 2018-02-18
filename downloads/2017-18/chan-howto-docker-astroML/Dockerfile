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
WORKDIR	/root

#==============================================================================
# Install Jupyter and other visualization packages
RUN	pip install jupyter ipywidgets &&\
	jupyter nbextension enable --py --sys-prefix widgetsnbextension

# By default we start a Jupyter Notebook
ADD     notebook.sh /
CMD     /notebook.sh

# To use Jupyter Notebook, run the following from the host:
#
#       docker run -it --rm -p8888:8888 chanchikwan/astroml
#                             ^dst ^src
#
# then use a browser to open
#
#       http://[localhost or ip of remote machine]:8888?token=1234...
#
# You can use ssh to tunnel the remote notebook to your local machine
#
#       ssh -NfL localhost:8888:localhost:8888 server
#                          ^dst           ^src
