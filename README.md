# RQS Argos - Extractor Setup

## Linux: Debian

Inside the folder ./, copy and paste on command line

```shell
sudo apt update
sudo apt upgrade
```

Exit command line. Then copy and paste on command line

```shell
# This
virtualenv venv
source ./venv/bin/activate
# Or this
python3 -m venv venv
source ./venv/bin/activate
```

Then copy and paste

```shell
python -m pip install --upgrade pip
pip install --upgrade cython
pip install wheel
pip install -r dev-requirements.txt
```

## Run program

```shell
(venv) .\> python src/main.py
```
