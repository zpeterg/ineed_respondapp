# ineed-respond-app
Community resources chat-bot python server

# Run
Based on: https://docs.djangoproject.com/en/2.1/intro/tutorial01/
1. Dev server: ```python manage.py runserver```
Access at ```192.168.99.100:8000```, or whatever the docker-machine ip is.
If changes, may need to update ```settings.py```->ALLOWED_HOSTS with new IP.

# Run Tests
Change environments: 
1. List environments: ```conda env list```
2. Activate environment: ```activate nlp```
Run tests (be sure to use the double-quotes):
```python -m unittest discover ./ "*test.py"```

# Send Postman Tests:
1. Create POST to: http://192.168.99.100:8000/chat/
2. Add Body of ```user_id```, ```phrase``` like 'child' and ```session``` like ['clothing']