openssl genpkey -out auth.pem -algorithm rsa -pkeyopt rsa_keygen_bits:2048 
openssl rsa -in auth.pem -out auth.pub -pubout

base64 auth.pem > auth.pem.b64
base64 auth.pub > auth.pub.b64
