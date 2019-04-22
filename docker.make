PANDOC := 2.7.2

pandoc:
	@wget -O pandoc.tar.gz https://github.com/jgm/pandoc/releases/download/$(PANDOC)/pandoc-$(PANDOC)-linux.tar.gz
	@tar -xf pandoc.tar.gz
	@cp pandoc-$(PANDOC)/bin/pandoc /usr/bin
	@rm -r pandoc-$(PANDOC)

tools:
	@poetry build --format=wheel
	@pip install dist/*.whl

.PHONY: pandoc tools
