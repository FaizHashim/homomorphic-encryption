FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN mkdir query_data
RUN mkdir factors_data
# RUN --mount=type=bind,src=tmp/data,target=/app/data 

CMD [ "python3" , "cs.py"]

EXPOSE 3000