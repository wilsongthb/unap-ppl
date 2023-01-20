# INSTALACION

Requiere min python 3.8

```
pip install -r requirements.txt
```

Ejecutar aplicacion
```
./manage.py migrate && ./manage.py flush && ./manage.py user_seed && ./manage.py marketplace_seed
./manage.py runserver
```
