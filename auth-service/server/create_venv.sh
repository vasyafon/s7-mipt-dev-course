python3.8 -m venv venv 
source ./venv/bin/activate
./venv/bin/pip3 install --upgrade pip wheel 
./venv/bin/pip3 install  --upgrade -r ./requirements.txt
./venv/bin/pip3 install -r ./requirements_custom.txt
./venv/bin/pip3 install  -r ./test-requirements.txt
