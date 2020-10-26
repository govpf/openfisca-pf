FROM python:3.7-slim AS build
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc git
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install wheel
WORKDIR /openfisca_main
RUN git clone https://github.com/openfisca/openfisca-core.git
WORKDIR /openfisca_main/openfisca-core
RUN sed -i s/float32/float64/ openfisca_core/variables.py
RUN pip install .
WORKDIR /openfisca_main
COPY openfisca_pf ./openfisca_pf
COPY Makefile .
COPY *.md .
COPY LICENSE .
COPY *.in .
COPY *.py ./

RUN make build

FROM python:3.7-slim
COPY --from=build /opt/venv /opt/venv
COPY --from=build /root/.cache/pip /root/.cache/pip
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /openfisca_main
COPY --from=build /openfisca_main/config.py .
COPY --from=build /openfisca_main/openfisca_pf ./openfisca_pf
EXPOSE 5000/tcp

CMD ["openfisca", "serve", "--configuration-file", "config.py"]
