# Sigemh

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/victoracioly/sigemh.git
cd sigemh
virtualenv env --python=python3
source env/bin/activate
pip install -r requirements_dev.txt
cp contrib/env-sample .env
python manage.py test

```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Define um SECRET_KEY segura para instância.
4. Defina DEBUG=True
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia

heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config set DEBUG=False

# Configure o email com sendgrid
heroku addons:create sendgrid:starter

heroku config:set EMAIL_HOST=smtp.sendgrid.com
heroku config:set EMAIL_PORT=587
heroku config:set EMAIL_USE_TLS=True
heroku config:set EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
heroku config:set EMAIL_HOST_USER=`heroku config:get SENDGRID_USERNAME`
heroku config:set EMAIL_HOST_PASSWORD=`heroku config:get SENDGRID_PASSWORD`

git push heroku master --force
```
