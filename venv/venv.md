create python venv
```
python -m venv venv_name
```
activate python venv
```
venv_name>Scripts\activate.bat
```
install package
```
(venv_name) venv_name>pip install package_name
```
generate a requirements file and then install from it in another environment
```
(venv_name) venv_name>pip freeze > requirements.txt
```
*requirements.txt*
```
*Django==2.2
pytz==2018.9
sqlparse==0.3.0*
```
```
pip install -r requirements.txt
```
deactivate python venv
```
(venv_name) deactivate
```
