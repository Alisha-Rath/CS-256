## Install requirements (Use python 3.11)
pip install -r /path/to/requirements.txt

## setup environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

## Run
flask run

(or)

python3 -m venv path/to/venv
source path/to/venv/bin/activate
to run : sudo python3 app.py
It will start running on localhost:5000/chat

## API key
https://openrouter.ai/models/mistralai/mistral-7b-instruct:free
update it in key.py

## Resume
Add resume in resume.txt
