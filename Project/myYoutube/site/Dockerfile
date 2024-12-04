FROM node:16

WORKDIR /usr/src/app

COPY package*.json ./

# Increase npm timeout and switch to a faster registry
RUN npm config set timeout 300000
RUN npm config set registry https://registry.npmjs.org/

# Install dependencies
RUN npm install

COPY . .

EXPOSE 3000
CMD ["npm", "start"]
