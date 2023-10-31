.PHONY: test
test:
	@pytest

.PHONY: setup
setup:
	@pip install pip==23.2.1
	@pip install wheel==0.41.2
	@pip install -e .
	@pip install -r requirements.txt

.PHONY: run
run:
	@bash run.sh