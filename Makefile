
.PHONY: env
env:
	virtualenv -p python3 env

.PHONY: bootstrap
bootstrap:
	pip install -r requirements.txt

.PHONY: shell
shell:
	ipython

.PHONY: test
test:
	python -m pytest tests/

.PHONY: run
run:
	python main.py

.PHONY: upgrade
upgrade:
	pip-compile --no-index --index-url https://pypi.python.org/pypi/ --upgrade

.PHONY: compile
compile:
	pip-compile --no-index --index-url https://pypi.python.org/pypi/

.PHONY: sync
sync:
	pip-sync --index-url https://pypi.python.org/pypi/
