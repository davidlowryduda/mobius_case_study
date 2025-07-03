PYTHON = python3

mobius.so: mobius.cpp
	g++ --std=c++17 -O3 -shared -o mobius.so -fPIC mobius.cpp

.PHONY: test
test: mobius.so
	$(PYTHON) -m unittest mobius_test.py

.PHONY: clean
clean:
	rm -r __pycache__/
