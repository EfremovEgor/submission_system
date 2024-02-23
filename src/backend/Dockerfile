FROM python:3.11-slim-buster as builder


WORKDIR /backend

COPY requirements/requirements.production.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.production.txt

COPY ./src ./src
COPY ./scripts ./scripts

WORKDIR /backend/src
ENTRYPOINT  [ "/bin/bash","/backend/scripts/docker-entrypoint.sh" ] 
# CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:80","--workers","4","--worker-class","uvicorn.workers.UvicornWorker"]

# FROM builder as dev-envs

# RUN <<EOF
# apt-get update
# apt-get install -y --no-install-recommends git
# EOF

# RUN <<EOF
# useradd -s /bin/bash -m vscode
# groupadd docker
# usermod -aG docker vscode
# EOF
# install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /