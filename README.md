# Setup

```bash
# python 3.8 or above will be required
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py
```

# How to use:

- Visit http://localhost:5000/apidocs/ and shorten a url using `/url/shorten` api
- Visit the given short url in response
- Visit http://localhost:5000/apidocs/ and shorten a url using `/url/analytics` api to get number of hits given url and client id