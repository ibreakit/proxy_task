HTTP_PORT ?= 8080

build:
	docker image build -t proxy-task .
run:
	docker run -d -p $(HTTP_PORT):5000 proxy-task
clean:
	rm -rf src/__pycache__