.PHONY: test
test:
	python api_numx.py
	#pytest

test2:
	poetry run pytest -rA -vvs --log-level INFO

test3:
	poetry run python api_dfx.py
