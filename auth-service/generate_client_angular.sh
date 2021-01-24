docker run --rm -v ${PWD}:/local -w /local --user $(id -u):$(id -g) openapitools/openapi-generator-cli generate \
    -c ./config_client_angular.yaml \
    -i ./authAPI.yaml \
    -g typescript-angular \
    -o ./client-angular-gen