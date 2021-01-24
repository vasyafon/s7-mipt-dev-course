rm -rf ./client-python-aiohttp-gen
docker run --rm -v ${PWD}:/local -w /local --user $(id -u):$(id -g) openapitools/openapi-generator-cli generate \
    -c ./config_client_simple_python.yaml \
    -i ./airport_load_api.yaml \
    -g python \
    -o ./client-python-gen \


