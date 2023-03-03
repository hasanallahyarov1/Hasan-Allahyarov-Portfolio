PYTHON 3.9

For using this code you need to install:

$ pip install --upgrade pip

$ pip install spacy

$ python -m spacy download en_core_web_sm

$ pip install flask

$ pip install uvicorn

$ pip install flask-restful

$ pip install streamlit

$ pip install fastapi

$ pip install pydantric

# RESTFUL API:

To run RESTFUL API:

uvicorn restful_api:app --reload

To use RESTFUL API:

For get request you should run:

curl http://127.0.0.1:8000/api

For post request you should run:

curl -X POST -H "Content-Type: application/json" -d '{"text": "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously. “I can tell you very senior CEOs of major American car companies would shake my hand and turn away because I wasn’t worth talking to,” said Thrun, in an interview with Recode earlier this week."}' http://127.0.0.1:8000/api


# FLASK

To run Flask webserver:

python app.py

To access it you should go to http://127.0.0.1:5000 on your browser

# Streamlit

To run Streamlit webserver:

streamlit run streamlit_ner_demo.py

It should open by itself, if no you should go to http://localhost:8501 on your browser



