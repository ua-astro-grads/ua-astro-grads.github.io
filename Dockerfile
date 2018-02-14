FROM    debian:stretch

RUN     apt-get -qq update &&\
        apt-get install -y python-pip &&\
        apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN     pip install --upgrade pip &&\
	pip install numpy scipy scikit-learn matplotlib astropy &&\
	pip install astroML astroML_addons

WORKDIR /root
