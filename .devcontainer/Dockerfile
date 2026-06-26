FROM python:3.12-slim

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000

RUN apt-get update && apt-get install -y \
    git curl ca-certificates build-essential bash sudo \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

RUN pip install --no-cache-dir uv

WORKDIR /workspace

USER ${USERNAME}

# Install Codex CLI for the vscode user
RUN curl -fsSL https://chatgpt.com/codex/install.sh | sh

# Make sure user-local binaries are available in PATH
ENV PATH="/home/${USERNAME}/.local/bin:/home/${USERNAME}/bin:${PATH}"