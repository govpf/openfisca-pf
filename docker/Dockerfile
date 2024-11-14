FROM python:3.14.0a1-slim AS build

ENV PATH="/opt/venv/bin:$PATH"

COPY docker/install_deps /install_deps
COPY docker/variables.patch /variables.patch
RUN python -m venv /opt/venv \
    && /install_deps

WORKDIR /openfisca_main
COPY openfisca_pf ./openfisca_pf
COPY Makefile .
COPY *.md ./
COPY LICENSE .
COPY *.in ./
COPY *.py ./
RUN make build

FROM python:3.14.0a1-slim
COPY --from=build /opt/venv /opt/venv
COPY --from=build /root/.cache/pip /root/.cache/pip
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /openfisca_main
COPY --from=build /openfisca_main/config.py .
COPY --from=build /openfisca_main/openfisca_pf ./openfisca_pf

CMD ["openfisca", "serve", "--configuration-file", "config.py"]
