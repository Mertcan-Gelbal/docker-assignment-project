# syntax=docker/dockerfile:1

FROM node:18-alpine AS base
WORKDIR /app
COPY package*.json ./

FROM base AS dev
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]

FROM base AS production
RUN npm ci --only=production && npm cache clean --force
COPY . .
USER node
EXPOSE 3000
CMD ["node", "src/index.js"] 