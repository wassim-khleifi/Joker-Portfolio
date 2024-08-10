# Joker Portfolio Deployment Tutorial:
### Setup for production:
* Switch to a production friendly database:
> In this example, we used postgresql. You can find other models here: [Click Me](https://docs.djangoproject.com/en/5.0/ref/databases/)
```py
# File Path: portfolio/settings.py

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'db_name',

        'USER': 'db_user',

        'PASSWORD': 'db_pass',

        'HOST': 'db_host',

        'PORT': 'db_port',

    }

}
```
* Turn Debug off:
```py
# File Path: portfolio/settings.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
```

### Recommended Hosts:
* [Pythonanywhere](https://www.pythonanywhere.com/)
* [Vercel](https://vercel.com/)
* [Render](https://render.com/)

### Support:
* For any additional support, contact me on discord (username: jock3r9).
