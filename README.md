# buzzword_bingo

Simple FastAPI scaffold with a frontend placeholder.

## Repository layout

- `app/` – frontend placeholder
- `api/` – backend scaffold (FastAPI)

## Checkout

```bash
git clone https://github.com/pl88/buzzword_bingo.git
cd buzzword_bingo
```

## Install

This project uses [uv](https://docs.astral.sh/uv/):

```bash
make install
```

## Run API

```bash
make run
```

The root endpoint is available at `http://127.0.0.1:8000/`.

## Validate

```bash
make lint
make typecheck
make test
```
