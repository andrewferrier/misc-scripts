build:
	docker build -t andrewferrier/draw.io .

run: build
	docker run -d -p 8080:80 andrewferrier/draw.io
	open 'http://localhost:8080/index.html?offline=1&https=0'
