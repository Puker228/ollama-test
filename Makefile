up:
	docker compose build
	docker compose down
	docker compose up -d

stop:
	@docker compose stop

format:
	ruff check --select I,F401 --fix
	ruff format
