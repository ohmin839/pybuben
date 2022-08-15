FROM python:3.7.13-slim

ARG UID=1000
ARG GID=1000
ARG USERNAME=user
RUN groupadd -g $GID $USERNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME

RUN apt-get update && \
    apt-get install -qy build-essential graphviz

COPY ./docker/deeplearning/entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]

USER $USERNAME
WORKDIR /pybuben-deeplearning
