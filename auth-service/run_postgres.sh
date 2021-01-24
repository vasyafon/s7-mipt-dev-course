export LOCAL_POSTGRES_PASSWORD="auth-postgres-password"
## 2. run the postgres image
docker rm auth-postgres
docker run -d \
	--name auth-postgres \
	-e POSTGRES_PASSWORD=$LOCAL_POSTGRES_PASSWORD \
    -e POSTGRES_USER=postgres \
    --shm-size=1g \
    -p 5439:5432 \
    postgres
docker start auth-postgres