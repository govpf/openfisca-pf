FROM python:3.7-slim AS build
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /openfisca_main
COPY openfisca_pf ./openfisca_pf
COPY Makefile .
COPY *.py ./
RUN make install
RUN ls -ltra /

FROM python:3.7-slim
COPY --from=build /opt/venv /opt/venv
COPY --from=build /root/.cache/pip /root/.cache/pip
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /openfisca_main
COPY --from=build /openfisca_main/config.py .
COPY --from=build /openfisca_main/openfisca_pf ./openfisca_pf

CMD ["openfisca", "serve", "--configuration-file", "config.py"]
EXPOSE 5000/tcp