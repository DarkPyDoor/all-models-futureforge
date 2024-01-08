# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Pillow using pip
RUN pip install Pillow

# Railway provides the PORT environment variable, so we do not need to EXPOSE a port
# However, you can still EXPOSE a port for local testing purposes
EXPOSE $PORT

# Use the PORT environment variable provided by Railway in the streamlit command
CMD ["sh", "-c", "streamlit run --server.port $PORT app.py"]
