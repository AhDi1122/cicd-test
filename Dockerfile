FROM docker.io/library/nginx:alpine

WORKDIR /usr/share/nginx/html
COPY index.html .
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

