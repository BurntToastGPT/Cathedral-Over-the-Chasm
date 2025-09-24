# Minimal, offline-friendly container for a hello-world run
FROM python:3.11-slim

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY harness/ ./harness/
COPY run_eval.sh ./run_eval.sh
RUN chmod +x /app/run_eval.sh
ENTRYPOINT ["/app/run_eval.sh"]
