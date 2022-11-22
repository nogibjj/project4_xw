install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	# python -m pytest -vv --cov=hello --cov=cli test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123396165066.dkr.ecr.us-east-1.amazonaws.com
	docker build -t project4 .
	docker tag project4:latest 123396165066.dkr.ecr.us-east-1.amazonaws.com/project4:latest
	docker push 123396165066.dkr.ecr.us-east-1.amazonaws.com/project4:latest

all: install test format lint deploy