all:
	python setup.py build
	python setup.py install_lib
	rm -rf build
