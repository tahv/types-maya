[private]
default:
  @just --list

image-name := "maya-stubs"

[private]
docker-build:
  docker build --platform linux/amd64 -t {{image-name}} .

# Run an interactive docker container
interactive: docker-build
  docker run -it --rm {{image-name}}
