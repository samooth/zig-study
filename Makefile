Z16 ?= <zvm-root>/0.16.0/zig
Z17 ?= <zvm-root>/0.17.0/zig

# Zig version manager root (zvm, not nvm). All stable Zig toolchains installed
# under <zvm-root>/: 0.10.1 0.11.0 0.12.0 0.13.0 0.14.0 0.16.0 0.17.0
# ZVM_ROOT must point to your local zvm installations (e.g. ~/.zvm).
# Adjust this default or override via `make ZVM_ROOT=/path/to/zvm ...`.
ZVM_ROOT ?= <zvm-root>
# Versions to regenerate/verify with `gen-all` / `verify-all`.
VERSIONS ?= 0.10.1 0.11.0 0.12.0 0.13.0 0.14.0 0.16.0 0.17.0

gen:
	python3 tools/gen.py --zig $(Z16)
	python3 tools/gen.py --zig $(Z17)

verify:
	python3 tools/verify.py --zig $(Z16)
	python3 tools/verify.py --zig $(Z17)

check-examples:
	python3 tools/check-skill-examples.py

check: gen verify check-examples

# Regenerate signature tables + HTML for every installed Zig version.
gen-all:
	@for v in $(VERSIONS); do \
		echo "=== gen $$v ==="; \
		python3 tools/gen.py --zig $(ZVM_ROOT)/$$v/zig || exit $$?; \
	done

# Verify generated artifacts for every installed Zig version.
verify-all:
	@for v in $(VERSIONS); do \
		echo "=== verify $$v ==="; \
		python3 tools/verify.py --zig $(ZVM_ROOT)/$$v/zig || exit $$?; \
	done

check-all: gen-all verify-all check-examples

.PHONY: gen verify check-examples check gen-all verify-all check-all
