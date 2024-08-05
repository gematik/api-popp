DOCKER_IMAGE=spilikin/popp-mock:latest


info:
	@echo "Available targets:"
	@echo "  requirements: generate requirements.txt"
	@echo "  dockerbuild: build docker image"
	@echo "  dockerpush: push docker image to registry"

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

dockerbuild: requirements
	docker buildx build --platform linux/amd64 -t $(DOCKER_IMAGE) .

dockerpush: dockerbuild
	docker push $(DOCKER_IMAGE)