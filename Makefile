version := $(shell grep version pyproject.toml | grep -o -E "\b[0-9]+\.[0-9]+\.[0-9]+\b")

release:
	git clean -dfX
	zip -r BNotebooks_$(version).zip BNotebooks -x *pycache* *.blend1
