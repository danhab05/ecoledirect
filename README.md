# EcoleDirect
github profile: https://github.com/snowy-27

### Description
Ecole direct is a script that can get data from the website https://www.ecoledirecte.com/
github link: https://github.com/Snowy-27/ecoledirect

### Installation
```sh
pip install ecoledirect
```
or 
```sh
pip install git+https://github.com/Snowy-27/ecoledirect
```

### Documentation

First Tab:
```py
from ecoledirect import EcoleDirect
user = EcoleDirect('username', 'password')
user.login()
```
```py
print(user.get_homework())
```
The function get notes is currently in developement. 
```py
print(user.get_notes()) 
```
At the end of the script: 
```py
user.close()
```
