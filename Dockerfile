FROM python:latest
ADD . /app
COPY pyproject.toml .
WORKDIR /app
#RUN cd /app
RUN pip install poetry
RUN pip install uvicorn
RUN pip install fastapi
RUN poetry add fastapi
RUN poetry add uvicorn
ENTRYPOINT uvicorn main:app --reload --host "0.0.0.0"
