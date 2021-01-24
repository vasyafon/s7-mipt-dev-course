python3.8 -m venv venv
source ./venv/bin/activate
./venv/bin/pip3 install --upgrade pip
./venv/bin/pip3 install wheel
./venv/bin/pip3 install -r ./requirements.txt
./venv/bin/pip3 install -r ./test-requirements.txt
