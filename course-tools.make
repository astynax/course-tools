RUN := @docker run --rm -u $$(id -u):$$(id -g) -v $$(pwd):/work -i astynax/course-tools

reorg:
	@$(RUN) reorg

scaffold:
	@$(RUN) scaffold

.PHONY: reorg scaffold
