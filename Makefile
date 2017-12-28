
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

.PHONY: upgrade
upgrade:
	pip-compile --no-index --upgrade

.PHONY: compile
compile:
	pip-compile --no-index
