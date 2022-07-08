init:
	pip install -r requirements.txt

main:
	python main.py

clean:
	rm -rf ./src/__pycache__