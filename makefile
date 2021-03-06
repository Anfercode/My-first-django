SHELL := /bin/bash

include .env

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
	python3 -m venv $(VENV) && source $(BIN)/activate

.PHONY: install
install: venv ## Make venv and install requirements
	$(BIN)/pip install -r requirements.txt

migrate: ## Make and run migrations
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

db-up: ## Pull and start the Docker Postgres container in the background
	docker rm -f  database
	docker-compose run --rm --service-ports --name database db

db-shell: ## Access the Postgres Docker database interactively with psql
	docker exec -it database psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

.PHONY: test
test: ## Run tests
	$(PYTHON) manage.py test application --verbosity=0 --parallel --failfast

.PHONY: run
run: ## Run the Django server
	$(PYTHON) manage.py runserver

start: install migrate run ## Install requirements, apply migrations, then start development server
