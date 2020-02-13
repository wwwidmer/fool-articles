#! /bin/bash

pip install pipenv

pipenv sync

touch .env

echo 'SECRET_KEY=supersecret' > .env

pipenv run migrate && pipenv run test && pipenv run dev
