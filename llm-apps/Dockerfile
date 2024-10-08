FROM python:3.11

WORKDIR /app

# Install all required libraries
COPY requirements.txt ./
RUN  pip install -r requirements.txt

# Copy resources
COPY  * ./

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "chat_app1_replicate.py", "--server.port=8501", "--server.address=0.0.0.0"]