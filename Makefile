.PHONY: help
help:  ## Show this help.
# Taken from https://stackoverflow.com/a/35730328/6925187
	@egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install:  ## Install dependencies
	python -m pip install --upgrade pip
	pip install -r requirements-dev.txt

.PHONY: install-bundle
install-bundle: ## Install the locally packaged swarmlib bundle (wheel)
	python -m pip install --upgrade pip
	pip install `find dist -iname '*.whl'`
	swarm --version

.PHONY: test
test:  ## Run tests
	pytest tests

.PHONY: lint
lint:  ## Lint
	pylint swarmlib tests

.PHONY: bundle
bundle: ## Bundle swarmlib
	cp ThirdPartyNotices.txt LICENSE.txt swarmlib
	python setup.py sdist bdist_wheel
	twine check dist/*
	rm swarmlib/ThirdPartyNotices.txt swarmlib/LICENSE.txt

.PHONY: clean
clean: ## Clean the project. Remove all cache/temporary files
# Taken from https://stackoverflow.com/a/41386937/6925187
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm -rf swarmlib.egg-info .coverage coverage.xml build dist .pytest_cache
