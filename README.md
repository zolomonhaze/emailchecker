# Emailchecker

Simple way to check email or bunch of emails with api. Thanks for <a href="https://isitarealemail.com">isitarealemail.com</a> the api.
You may need to register the site and get your own api key

pip3 install csv, requests, argparse

# Features

* Check one email
* Check bunch of emails in file ex. emails.csv

# Examples

```
python3 emailchecker.py -e example@gmail.com
```

```
python3 emailchecker.py -w emails.csv
```

# How it works?

Tell me tell about it. Service checks is the address syntacitcally correct, it checks does the email server exist and does that address exit in that server.
