build:
	python3 cpo.py

testCase:
	pytest test_cpo.py

testSample:
	cat sample1.in | python3 cpo.py | diff - sample1.ans

checkStyles:
	flake8 cpo.py 
	flake8 test_cpo.py

fixStyles:
	autopep8 --in-place --aggressive --aggressive cpo.py
	autopep8 --in-place --aggressive --aggressive test_cpo.py

checkTypes:
	mypy cpo.py 
	mypy test_cpo.py

kattis:
	kattis -f cpo.py -p cosmicpathoptimization

all:
	make testCase
	make testSample
	make checkStyles
	make fixStyles
	make checkTypes
	make kattis
	