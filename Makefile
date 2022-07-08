init: requirements.txt
	pip install -r requirements.txt

main:
	python main.py

clean:
	rm -rf ./src/__pycache__