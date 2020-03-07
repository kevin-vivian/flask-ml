virtualenv -p `which python3` venv
source venv/bin/activate
pip3 install -r ~/flask_rest_ml/requirements.txt
python3 setup.py develop
