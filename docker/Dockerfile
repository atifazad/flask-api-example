FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

# Create application root directory in container
RUN mkdir /dockerised-example

# Set dockerised-example as working directory
WORKDIR /dockerised-example

# Copy requirements.txt in application root directory
ADD requirements.txt /dockerised-example/

RUN \
    # Install curl
    apk add --no-cache curl && \
    # Install postgres utilities which are required by `psycopg2` lib being used by app
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    # Install Python packages required by the app
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

# Add all files from current directory on host to dockerised-example directory in container 
ADD ./ /dockerised-example/
COPY docker/entrypoint.sh /sbin/entrypoint.sh

EXPOSE 5000

# Execute command when container starts
ENTRYPOINT ["/sbin/entrypoint.sh"]
