DATE := $(shell date '+%Y%m%d')
IMAGETAG := 'andrewferrier/draw.io'

build:
	docker build -t $(IMAGETAG) .
	docker tag $(IMAGETAG) $(IMAGETAG):$(DATE)

run: build
	nohup docker run --rm -p 8080:80 --name draw.io $(IMAGETAG) &
	open 'http://localhost:8080/index.html?offline=1&https=0'
