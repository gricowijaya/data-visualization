init: requirements.txt
	pip install -r requirements.txt

run:
	python main.py

clean:
	rm -rf ./src/__pycache__