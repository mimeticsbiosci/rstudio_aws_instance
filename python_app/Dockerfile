FROM python:3.13

WORKDIR /app

RUN pip install --upgrade pip && pip install Flask python-dotenv gunicorn requests

COPY python_app/form/ python_app/form/

EXPOSE 8000

WORKDIR /app/python_app

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0", "form:create_app()"]
