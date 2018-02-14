hub_id = chanchikwan

build:
	docker build -t $(hub_id)/astroml .

push:
	docker push $(hub_id)/astroml

bash:
	docker run -it --rm -v `pwd`:/root $(hub_id)/astroml bash

jupyter:
	docker run -p8888:8888 --rm -v `pwd`:/root $(hub_id)/astroml &
