init: requirements.txt
	pip install -r requirements.txt

run:
	python main.py

testing:
	python ./testing/testing.py 

clean:
	rm -rf ./src/__pycache__
