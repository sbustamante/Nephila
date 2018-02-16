init:
	pip install -r requirements.txt

edit:
	kate ./nephila/*.py &

test:
	nosetests tests
