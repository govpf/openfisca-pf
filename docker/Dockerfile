# FROM python:3.7 AS build
# WORKDIR /openfisca_pf
# COPY openfisca_pf .
# COPY Makefile .
# COPY openfisca .
# COPY *.py ./
# RUN make install


# FROM python:3.7
# WORKDIR /openfisca_pf
# COPY --from=build openfisca_pf ./
# CMD ["ls", "-l"]
# CMD ["./openfisca", "serve", "--configuration-file", "config.py"]
# openfisca serve --configuration-file config.py

FROM python:3.7
WORKDIR /openfisca_main
COPY openfisca_pf ./openfisca_pf
COPY Makefile .
# COPY openfisca .
COPY *.py ./
RUN make install
CMD ["openfisca", "serve", "--configuration-file", "config.py"]
EXPOSE 5000/tcp