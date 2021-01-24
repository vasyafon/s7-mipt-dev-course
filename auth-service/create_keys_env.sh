openssl genpkey -out temp/auth.pem -algorithm rsa -pkeyopt rsa_keygen_bits:2048 
openssl rsa -in temp/auth.pem -out temp/auth.pub -pubout
base64 -w0 temp/auth.pem > temp/auth.pem.b64
base64 -w0 temp/auth.pub > temp/auth.pub.b64
echo AUTH_PRIVATE_KEY="$(cat temp/auth.pem.b64)" > temp/.env
echo AUTH_PUBLIC_KEY="$(cat temp/auth.pub.b64)" >> temp/.env
