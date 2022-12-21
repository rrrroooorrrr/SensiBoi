FROM python:3.8-alpine

# Install required packages and libraries
RUN apk add --no-cache git

# Install the required Python packages
RUN pip install discord nltk textblob python-dotenv tweepy

# Create a working directory
WORKDIR /app

# Copy the source code into the working directory
COPY . .

# Run the Discord bot
CMD ["python", "sensi_boi.py"]