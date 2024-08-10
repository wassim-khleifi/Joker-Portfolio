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
* [Pythonanywhere](https://www.pythonanywhere.com/) | Details: [Article](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
* [Vercel](https://vercel.com/) | Details: [Article](https://vercel.com/templates/python/django-hello-world)
* [Render](https://render.com/) | Details: [Article](https://docs.render.com/deploy-django)

### Support:
* For any additional support, contact me on discord (username: jock3r9).

### Donation:
If you love the portfolio, feel free to support me:

<a href='https://ko-fi.com/jock3r9'><img src='https://ko-fi.com/img/githubbutton_sm.svg' height="27px"/></a>
