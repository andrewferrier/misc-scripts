build:
	docker build -t andrewferrier/draw.io .

run: build
	nohup docker run --rm -p 8080:80 --name draw.io andrewferrier/draw.io &
	open 'http://localhost:8080/index.html?offline=1&https=0'
