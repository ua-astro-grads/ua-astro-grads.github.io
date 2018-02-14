hub_id = chanchikwan
server = ew

build:
	docker build -t $(hub_id)/astroml .

push:
	docker push $(hub_id)/astroml

bash:
	docker run -it --rm -v `pwd`:/root $(hub_id)/astroml bash

jupyter:
	docker run -it -p8888:8888 --rm -v `pwd`:/root $(hub_id)/astroml

tunnel:
	ssh -NfL localhost:8888:localhost:8889 $(server)
