init:
	pip install -r requirements.txt
dev:
	docker-compose -f docker-compose.dev.yml up --build
freeze:
	pip freeze > requirements.txt
prod:
	docker build -t shuttle-tracking:prod .
	docker run -d --rm -p 80:3000 shuttle-tracking:prod 
