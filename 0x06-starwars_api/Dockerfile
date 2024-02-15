# Use official Node.js 10 image as the base image
FROM node:10

# Set working directory inside the container
WORKDIR /app

RUN npm install semistandard --global
RUN npm install request --global

RUN npm install

## Copy package.json and package-lock.json to the working directory
#COPY package*.json ./

# Install dependencies


# Copy the rest of the application code to the working directory
COPY . .

# Expose port 3000 (or any other port your application uses)
EXPOSE 3000

# Command to run the script when the container starts
CMD ["node", "0-starwars_characters.js"]
