# Business Intelligence Automation

This repository contains the work done for automating the business intelligence services provided at OpenSourcePolitics.

## Architecture

The repository is composed of three parts :
- a `Matomo` folder handles the connection with the remote Matomo instance of OSP, providing basic metadata about visitors' behaviour
- a `Metabase` folder does the same with the same with the remote instance of Metabase, providing basic metadata about democratic participation
- a `Google Docs` folder handles the connection with the remote Google Drive instance of OSP, making it possible to create, modify and delete files.

These 3 tool are wrapped in the `main.py` file, which aims to coordinate the data gathered from Matomo and Metabase and inject them in Google Drive files.

## Getting started
- Pull the repo
- Download the `credentials.json` file provided by the Google Drive API and paste it in `google_docs` folder
- Fill the credentials of `Matomo` in `matomo/secrets.yml` : url, site id, and authentication token when needed
- Fill the credentials of `Metabase` in `metabase/secrets.yml` : username, password and url

You're good to go !

## TODO
- [] Add tests
  - [] matomo
  - [] metabase
  - [] google docs/drive
- [] normalize functions that catch data
- [] normalized google docs functions 