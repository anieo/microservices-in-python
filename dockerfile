From python:alpine3.15
WORKDIR /app
COPY requirments.txt .
RUN pip install -r requirments.txt
COPY src src
EXPOSE 5005
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
            CMD curl -f http://localhost:5005/health || exit 1
ENTRYPOINT [ "python", "./src/app.py" ]