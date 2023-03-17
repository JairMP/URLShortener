# Explain

I choose an API Rest because for this simple API it works pretty well, plus it's neat, easy to read, and scalable. Use flask because it is a simple development, the simplicity of flask is perfect and python because it is a simple language that allows you to program faster and has a great community behind it.

# Documentation

## Installation

Setup a virtualenv and activate (On project Folder).

```sh
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

Setup the project.

```sh
make setup
```

## Start API

To start the API run.

```sh
make start
```

## Test

Run Tests.

```sh
make test
```

## Lint

Lint Format.

```sh
make lint
```

## Endpoints

#### Make an URL shorter:

```sh
POST http://127.0.0.1:5000/url/shortener/
```
You most send a JSON payload with url you want to make shorter.

```json
{
  "url": "www.google.com"
}
```
Response:

```json
{
  "message": "success", 
  "short_url": "www.short.com/g3VTbiEy6b"
}
```

#### Get the original url:

```sh
GET http://127.0.0.1:5000/url/shortener/?url=shorterUrl
```
You most send a url parameter with a valid shortUrl

```sh
www.short.com/7WLhWzwxQg
```

Response:

```json
{
  "message": "success", 
  "url": "www.google.com"
}
```