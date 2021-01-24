rm -rf ./client-python-aiohttp-gen
docker run --rm -v ${PWD}:/local -w /local --user $(id -u):$(id -g) openapitools/openapi-generator-cli generate \
    -c ./config_client_aiohttp_python.yaml \
    -i ./authAPI.yaml \
    -g python-legacy \
    -o ./client-python-aiohttp-gen \
    --library asyncio 

