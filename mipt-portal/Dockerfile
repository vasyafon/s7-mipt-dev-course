FROM node:12 AS builder
WORKDIR /opt/ng
COPY .npmrc package.json package-lock.json ./
RUN npm install
RUN npm install @angular/cli -g
COPY . ./
ARG CONFIGURATION
RUN bash -c 'echo -e $CONFIGURATION'
RUN ng build --configuration $CONFIGURATION

FROM nginx:1.17.10 as target
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /opt/ng/dist/mipt-portal /usr/share/nginx/html
ENV USER=65534
RUN chown -R $USER:$USER /usr/share/nginx/html && chmod -R 755 /usr/share/nginx/html && \
        chown -R $USER:$USER /var/cache/nginx && \
        chown -R $USER:$USER /var/log/nginx && \
        chown -R $USER:$USER /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R $USER:$USER /var/run/nginx.pid

