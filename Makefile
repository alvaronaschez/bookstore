run:
	poetry run uvicorn app.main:app

# start-alembic:
# 	poetry run alembic init alembic

make-migration:
	poetry run alembic revision -m "$(message)"

migrate:
	poetry run alembic upgrade head

test:
	poetry run pytest

build-docs:
	npx redoc-cli build openapi.json
