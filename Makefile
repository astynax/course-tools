NAME := course-tools:latest
REPO := astynax/$(NAME)

build:
	@docker build -t $(NAME) .

push:
	@docker push $(REPO)

tag:
	@docker tag $(NAME) $(REPO)

.PHONY: build push tag
