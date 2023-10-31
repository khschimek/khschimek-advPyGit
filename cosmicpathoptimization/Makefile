build:
	python3 cpo.py

testCase:
	pytest test_cpo.py

kattisLocal:
	cat 1.in | python3 cpo.py | diff - 1.ans

checkStyles:
	flake8 cpo.py 
	flake8 test_cpo.py

fixStyles:
	autopep8 --in-place --aggressive --aggressive cpo.py
	autopep8 --in-place --aggressive --aggressive test_cpo.py

checkTypes:
	mypy cpo.py 
	mypy test_cpo.py

testAll:
	make testCase
	make kattisLocal
	make checkStyles
	make fixStyles
	make checkTypes
	