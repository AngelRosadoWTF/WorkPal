FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install poetry && poetry install --no-root
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
