FROM astral/uv:python3.12-bookworm-slim
WORKDIR /usr/local/app

COPY . .
RUN uv sync
RUN uv run python manage.py migrate
EXPOSE 8000

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
