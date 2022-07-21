init: requirements.txt
	pip install -r requirements.txt

purge: requirements.txt
	pip uninstall -r requirements.txt

run:
	python main.py

testing:
	python ./testing/testing.py 

clean:
	rm -rf ./src/__pycache__

data-woman: 
	jupyter notebook ./Woman.ipynb

data-man: 
	jupyter lab ./resource/csv/man-fashions.csv

data-electronics: 
	jupyter lab ./resource/csv/electronics.csv
