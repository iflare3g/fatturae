# Fatture Elettroniche

> A small django web app to generate and store electronic invoices as required
> by the "Disegno di Legge di Bilancio 2018"

The app is built using Django and Python 3.7. It will provide a REST API that
will be used to generate the invoices XMLs, send them to the SdI and to archive
them.

Archivation will be done using django storages, so you can plug any storage
backend you like.

This project is under active development, current TODOs are:

-   [ ] generate invoice with real data from django models
-   [ ] create a REST API to generate, send and archive the invoice
-   [ ] add CI and deploy setup
-   [ ] more

NOTE: this is being worked for PyCon Italy, so the focus will be on having the
minimum functionality required for selling tickets for PyCon Italy, if you need
more features feel free to send a PR

## Installation

Install ```pipenv```

- ``` pipenv install --dev```

To get a fresh virtualenv with
all of dependencies needed for development.

Install ``docker``

Run

- ``docker-compose up -d``

to get database up and running

Run tests with

- ``pipenv run pytest``

Run django  inside project folder with 

``pipenv run ./manage.py runserver``
