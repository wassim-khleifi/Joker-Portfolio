<img src= "demo.png">

![Downloads](https://img.shields.io/github/downloads/Jock3r99/Joker-Portfolio/total.svg)
![License](https://img.shields.io/github/license/Jock3r99/Joker-Portfolio.svg)
![size](https://img.shields.io/github/repo-size/Jock3r99/Joker-Portfolio)
<img alt="Bitbucket open issues" src="https://img.shields.io/bitbucket/issues/Jock3r99/Joker-Portfolio">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Joker-Portfolio">

# Joker Portfolio


> A Joker theme portfolio to share your skills and projects around people!

## Features
  * Easy to run
  * Includes admin page
  * No external keys needed
  * portfolio.config.json File So You Dont Need To Edit The Code
  * Clean and smooth Design
  * The website is responsive for PC/Tablet and Mobile
  * More Updates In Future
### Requirements
  * Python +3.8V
  * Django
  * Virtualenv
### Setup
 1. Clone the repository:
 ```
git clone https://github.com/ashish-makes/django-tailwind-blog.git
 ```
 2. Navigate to the project directory:
```
 cd `django-tailwind-blog`
```
 3. Create and activate a new virtual environment:
```
 python -m venv env
 source env/bin/activate
```
  4. Install the project dependencies:
 ```
  pip install -r requirements.txt
 ```

 5. Editing the portfolio:
```json
  {
  "Config": {
    "name": "your name",
    "country": "your country",
    "avatar": "your avtar url",
    "introduction": "",
    "links": {
      "github": "https://github.com/",
      "reddit": "https://reddit.com/",
      "twitter": "https://twitter.com/",
      "discord": "https://discord.com/"
    },
    "contact": {
      "email": "example@gmail.com",
      "discord": "username",
      "webhook_url": "discord webhook url"
    }
  }
}

```
 6. Collect static files:
```python
python manage.py collectstatic
```
 7. Create the database tables:
```python
python manage.py makemigrations
python manage.py migrate
```
 8. Create admin super user:
```python
python manage.py createsuperuser
```
 9. Running the project
```python
python manage.py runserver
```
