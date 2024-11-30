# Name: Ahmed (Nur) Hassan
# User ID: Hass0338
# Assignment: NET2008 - Fall 2024 - Assignment 4
# Student Number: 040917085
# Date: 11/25/2024

# Base image with Python
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY coin_toss.py /app/

# Command to run the application
CMD ["python", "coin_toss.py"]
