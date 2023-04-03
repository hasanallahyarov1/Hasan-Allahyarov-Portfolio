PYTHON 3.9

For using this code you need to install:

Run docker

Create docker image

`docker build -t my-flask-app .`

Run container

`docker run -p 5000:5000 my-flask-app`

OR WITHOUT DOCKER


`$ pip install --upgrade pip`

`$ pip install spacy`

`$ python -m spacy download en_core_web_sm`

`$ pip install flask`
 
`$ pip install flask_sqlalchemy`

To Run code

`python app1.py`

To access it you should go to http://127.0.0.1:5000 on your browser


