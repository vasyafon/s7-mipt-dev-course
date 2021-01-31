# s7-mipt-dev-course
Repository for materials on MIPT-S7 course 'Kickstart to analytical aviary prototypes development'

# Steps to deploy the examples
- get google_env file from your professor and put it into repository directory
- run `create_keys_env.sh` in auth-service directory
  if running on Mac OS, remove `-w0` from 4th and 5th line of the script
- run `deploy_portal.sh` to deploy portal application, or `deploy_airport_load.sh` to deploy Airport load application
- open http://localhost:4200 in your browser
