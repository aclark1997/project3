FROM python:latest
ADD . /app
COPY pyproject.toml .
WORKDIR /app
#RUN cd /app
RUN pip install poetry
RUN pip install uvicorn
RUN pip install fastapi
RUN pip install "sqlalchemy[asyncio]"
RUN pip install asyncpg
RUN poetry add fastapi
RUN poetry add uvicorn
RUN poetry add "sqlalchemy[asyncio]"
RUN poetry add asyncpg
ENTRYPOINT uvicorn main:app --reload --host "0.0.0.0"
