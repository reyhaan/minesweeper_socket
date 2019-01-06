# ShuttleUp Tracking

Realtime location tracking for ShuttleUp

### Setup Prerequisites
* Python >= 3.7 - [Install](https://www.python.org/downloads/release/python-372/)
* Pip - [Install](https://pip.pypa.io/en/stable/installing/)
* Docker - [Install](https://docs.docker.com/install/)

### Setup Instructions
* Fork the repo
* Clone the repo by running the following command
```shell
git clone https://github.com/tktaofik/shuttle-tracking.git
cd shuttle-tracking
```
* Change git remote origin to your fork and upstream to this repo
```shell
git remote set-url origin https://github.com/USERNAME/shuttle-tracking.git
git remote add upstream https://github.com/tktaofik/shuttle-tracking.git
```
> replace USERNAME with your github username
* Create virtual environment and activate
```shell
python3 -m venv venv
source ./venv/bin/activate
```
* Install dependencies
```shell

make init
```

If you've made it here, you're all set!

### Running the application 
* It as simple as running the following command
```
make dev
```
