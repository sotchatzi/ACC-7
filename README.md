## Applied Cloud Computing 2020 Project Group 7   
Angle of Attack in Airfoil Simulations

## In general
- Container --> Docker, prebuilt image on Docker Hub

- Contextualisation --> OpenStack API (Novaclient)

- Web service --> Flask + templates, file storage

- Task Queue --> Celery + RabbitMQ, Redis

## Master setup
- `master_setup.txt` (a guide to set everything on a master node)
- `redis.conf`

## Application Service
- `flask_app.py`
- `templates/index.html`
- `result/`

## Task Queue
- `tasks.py` (this is not necessary, as the real working one is in the cloudinit script)

## Airfoil Service
- `image_build\*` (used to build the image with everything being ready)
- `Contextualisation\*` (to provision, the SNIC authentication step needs to be done)
