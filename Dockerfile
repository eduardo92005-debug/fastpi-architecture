FROM python:3.9-alpine
WORKDIR app/core
RUN pip install requirements.txt
CMD [“python”, “./main.py”] 
