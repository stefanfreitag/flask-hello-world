# First stage
FROM python:3.10 AS builder
COPY requirements.txt .

# Install dependencies to the local user directory
RUN pip install --user -r requirements.txt

# Second stage
FROM python:3.10-slim
LABEL maintainer="stefan@stefreitag.de"
WORKDIR /code

# Copy from first stage only the dependencies to the image
COPY --from=builder /root/.local/ /root/.local
COPY ./src .

# Update PATH environment variable
ENV PATH=/root/.local/bin:$PATH

CMD [ "python", "./server.py" ]
