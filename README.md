# I don't even go to that gym lol

![image](https://user-images.githubusercontent.com/76447395/234918992-7a8d5d25-cdfe-4cab-900c-07abdeddcb7a.png)

```
usage: bot.py [-h] -u USER -p PASSWORD [-l LIST] [-x PREFERENCIAS] [-b LOOP]

options:
  -h, --help            show this help message and exit
  -u USER, --user USER  Username
  -p PASSWORD, --password PASSWORD
                        PIN to login
  -l LIST, --list LIST  List available schedule (Y/N)
  -x PREFERENCIAS, --preferencias PREFERENCIAS
                        "MU002,MU003,MU025,MU026,MU053,MU054"
  -b LOOP, --loop LOOP  Intentarlo hasta que esté disponible (Y/N)
```

Example 

# How to list available schedules
```
python3 bot.py -u DNI -p PASS -l Y
```

# How to use
```
python3 bot.py -u DNI -p PASS -x "MU002,MU003,MU025,MU026,MU053,MU054"
```

# You can bruteforce adding the flag :

```
-b Y
```
