
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
