PYTHON = python3

.PHONY: usage
usage:
	@echo "USAGE"
	@echo "  good_data"
	@echo "  corrupted_data"
	@echo "  shuffle"
	@echo "  clean"


.PHONY: mobius
mobius:
	make -C ../mobius_code mobius.so

good_data: mobius
	mkdir -p ../../input
	$(PYTHON) generate_datafiles.py
	touch good_data

corrupted_data: mobius
	mkdir -p ../../input
	$(PYTHON) generate_corrupted_datafiles.py
	touch corrupted_data

shuffle: good_data
	$(PYTHON) shuffle_datafiles.py
	touch shuffle

.PHONY: clean
clean:
	rm -f good_data
	rm -f corrupted_data
	rm -f shuffle
	rm -r __pycache__/
