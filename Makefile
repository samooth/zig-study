Z16 ?= /home/t0m4s/.zvm/0.16.0/zig
Z17 ?= /home/t0m4s/.zvm/0.17.0/zig

gen:
	python3 tools/gen.py --zig $(Z16)
	python3 tools/gen.py --zig $(Z17)

verify:
	python3 tools/verify.py --zig $(Z16)
	python3 tools/verify.py --zig $(Z17)

check: gen verify

.PHONY: gen verify check
