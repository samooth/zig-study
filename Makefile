Z16 ?= /home/t0m4s/.zvm/0.16.0/zig
Z17 ?= /home/t0m4s/.zvm/0.17.0/zig

gen:
	python3 tools/gen.py --zig $(Z16)
	python3 tools/gen.py --zig $(Z17)

verify:
	python3 tools/verify.py --zig $(Z16)
	python3 tools/verify.py --zig $(Z17)

check-examples:
	python3 tools/check-skill-examples.py

check: gen verify check-examples

.PHONY: gen verify check-examples check
