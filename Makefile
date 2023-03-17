start:
	flask --app app run
test:
	pytest
setup:
	pip install -r requirements.txt
lint:
	black --exclude '\.git|\.mypy_cache|\.instance|\.migrations|\.env|env|Makefile|\.venv|venv' .
check-lint:
	black --check --exclude '\.git|\.mypy_cache|\.instance|\.migrations|\.env|env|Makefile|\.venv|venv' .