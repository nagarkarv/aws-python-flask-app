echo "Invoked afterinstall"
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt