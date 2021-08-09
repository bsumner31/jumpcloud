FROM python:3.7-alpine

WORKDIR /usr/src/app

RUN pip install --no-cache-dir requests

COPY . .

HEALTHCHECK --interval=12s --timeout=10s --start-period=30s \
  CMD curl --fail https://1df32474-ea60-4742-8cb9-a424d74647c0.mock.pstmn.io/manage_file || exit 1

CMD [ "python", "./service.py" ]