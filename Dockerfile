# Use a lightweight Linux base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the agent script into the container
COPY agents/health_agent.py .
RUN pip install psutil

# Run the agent
CMD ["python", "health_agent.py"]