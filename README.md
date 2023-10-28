# Product Recommendation System for DM

Its is a microservice which seeks for similar products based on their description


## Installation

1. Set the next environment variables inside of .env file in ***src/*** dir:
```
    DJANGO_SECRET_KEY
```

2. Install dependencies within your virtual environment:
```
    pip install requirements/dev.txt
```

3. Go to ***src/*** dir and run:
```
    python manage.py runserver
```

4. Create a superuser and register a new application to get CLIENT_ID, CLIENT_SECRET. 


5. Write the next variables into .env in DM project:
- CLIENT_ID
- CLIENT_SECRET
- USERNAME
- PASSWORD


## References
![Django Oauth](https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/rest-framework.html)