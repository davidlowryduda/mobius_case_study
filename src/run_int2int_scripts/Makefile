
.PHONY: data
data:
	make -C ../scripts/ shuffle

.PHONY: run
run: data
	bash int2int_mu.sh
	bash int2int_musq.sh

.PHONY: run-cpu
run-cpu: data
	bash int2int_mu_cpu.sh
