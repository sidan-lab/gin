
cov: ## check code coverage
	poetry run pytest -n 4 --cov sidan_gin

cov-html: cov ## check code coverage and generate an html report
	poetry run coverage html -d cov_html
	$(BROWSER) cov_html/index.html

test: ## runs tests
	poetry run pytest -vv

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr cov_html/
	rm -fr .pytest_cache

docs: ## build the documentation
	poetry export --dev --without-hashes > docs/requirements.txt
	rm -r -f docs/build
	poetry run sphinx-build docs/source docs/build/html
	$(BROWSER) docs/build/html/index.html

lint:
	poetry run flake8 src --ignore E501 --exclude src/sidan_gin/python_signing_module

format: ## runs code style and formatter
	poetry run isort .
	poetry run black .

deps:
	poetry lock
	poetry install

init:
	git submodule init
	git submodule update --force
	chmod +x ./src/sidan_gin/python_signing_module/build.sh
	cd ./src/sidan_gin/python_signing_module && ./build.sh