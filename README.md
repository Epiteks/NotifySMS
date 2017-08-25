# NotifySMS

🔔 ➡ 📱 Get Epitech notifications by SMS via Free Mobile

## How to use it ?

#### Setup

You need to set these variables into your environment :
- SMS_LOGIN
- SMS_TOKEN
- EPITECH_MAIL
- EPITECH_PWD

`SMS_*` are used by [`freemobilesms`](https://github.com/hug33k/freemobilesms).
You can get these infos in your [Free Mobile panel](https://mobile.free.fr/moncompte/)

`EPITECH_*` are used to log you in via [our wrapper](https://github.com/epiteks/wrapitech).

Example :
````bash
export SMS_LOGIN=xxxxxxx
export SMS_TOKEN=xxxxxxx
export EPITECH_MAIL=login_x@epitech.eu
export SMS_TOKEN=unix_pwd
````

Then you will need to install needed packages via [`pip`](https://pip.pypa.io/en/stable/installing/).
````bash
$> pip install -r requirements.txt
````

#### Let's run it

You will have to add a line to your `crontab` config.

````sh
$> crontab -e
````

Then you need to add this (Based on how often you want to run it and where `NotifySMS` is located on your computer) :

````
15 * * * * python3.5 $PATH_TO_NOTIFYSMS/main.py
````

(Here, it will run every 15 minutes `NotifySMS`, which is at $PATH_TO_NOTIFYSMS` location)

## FAQ

#### What about other mobile network operators ?

Since I am using Free Mobile, I can't implement other services.

But feel free to contribute !

#### I can't login, what can I do ?

Unfortunately, we don't support OAuth with [Wrapitech](https://github.com/epiteks/wrapitech).

Once again, feel free to contribute !`

#### What is `history.json` ? Can I delete it ?

This file is our "database". It stores the notifications you already got.

If you delete it, you will get a lot of messages next time you will run it.