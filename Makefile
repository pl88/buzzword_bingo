.RECIPEPREFIX = >
.PHONY: install run test lint typecheck

install:
>cd api && uv sync --group dev

run:
>cd api && uv run uvicorn my_api.main:app --reload

test:
>cd api && uv run pytest -q

lint:
>cd api && uv run ruff check src tests

typecheck:
>cd api && uv run pyright
