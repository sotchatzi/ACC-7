#!/bin/bash
docker run -td -v $(pwd):/home/fenics/shared -w /home/fenics/shared quay.io/fenicsproject/stable:current
docker ps -q > docker_id.txt
docker cp murtazo.tgz $(cat docker_id.txt):/home/fenics/shared/.
docker cp commands_container.sh $(cat docker_id.txt):/home/fenics/shared/.
docker cp runme.sh $(cat docker_id.txt):/home/fenics/shared/.
docker exec $(cat docker_id.txt) /home/fenics/shared/commands_container.sh
