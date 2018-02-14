hub_id = chanchikwan

build:
	docker build -t $(hub_id)/astroml .

push:
	docker push $(hub_id)/astroml

run:
	docker run -it --rm -v `pwd`:/root $(hub_id)/astroml
