You will need to create a `.env` file in the project root folder containing the application's configuration:

```dotenv
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=password
```

Then, build the docker image for the application:

```commandline
docker build . -t peckin-pairs
```

To spin up the application:

```commandline
docker run -it --rm -v./peckin_pairs:/usr/local/app/peckin_pairs -v./game:/usr/local/app/game  -p 8000:8000 peckin-pairs:latest
```

then, visit the url (http://127.0.0.1:8000) or the admin url (http://127.0.0.1:8000/admin) and log in using the
superuser username and password configured in your `.env` file above.

To run the `behave` tests, you will need to first install the dev dependencies

```commandline
uv sync --dev
```

and then run the tests with

```commandline
uv run behave
```
