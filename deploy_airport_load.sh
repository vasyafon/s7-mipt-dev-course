# read -s -p "Enter Google Client ID: " id
# read -s -p "Enter Google Client SECRET: " secret
# docker-compose build
. google_env
GOOGLE_CLIENT_ID=${id} GOOGLE_CLIENT_SECRET=${secret} docker-compose -f airport-load.docker-compose.yaml up 