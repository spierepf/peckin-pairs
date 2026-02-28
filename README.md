Start by building the docker image for the application:
```commandline
docker build . -t peckin-pairs
```

To spin up the application:
```commandline
docker run -it --rm -p 8000:8000 peckin-pairs:latest
```

then, visit the url: http://127.0.0.1:8000


To run the `behave` tests, you will need to first install the dev dependencies

```commandline
uv sync --dev
```

and then run the tests with

```commandline
uv run behave
```
