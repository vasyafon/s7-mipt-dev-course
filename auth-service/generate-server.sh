docker run --rm -v ${PWD}:/local -w /local --user $(id -u):$(id -g) openapitools/openapi-generator-cli generate \
    -c ./config_server.yaml \
    -i ./authAPI.yaml \
    -g python-aiohttp \
    -o ./server-gen
    