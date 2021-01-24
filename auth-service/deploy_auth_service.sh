read -s -p "Enter Google Client ID: " id
read -s -p "Enter Google Client SECRET: " secret
docker-compose build
GOOGLE_CLIENT_ID=${id} GOOGLE_CLIENT_SECRET=${secret} docker-compose up 