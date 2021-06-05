FROM node:15.12.0-alpine as frontend
WORKDIR /app
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM nginx:1.19.7-alpine
COPY --from=frontend /app/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"] 