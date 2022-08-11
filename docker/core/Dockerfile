FROM python:3.7.13-slim

ARG UID=1000
ARG GID=1000
ARG USERNAME=user
RUN groupadd -g $GID $USERNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME

COPY ./docker/core/entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]

USER $USERNAME
WORKDIR /pybuben-core
