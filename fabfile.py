from fabric.api import local


def deploy():
    commands = [
        "git push heroku master --force",
        "heroku run python manage.py migrate",
        "heroku open"
    ]

    local(' && '.join(commands))
