# NotifySMS

[![](https://images.microbadger.com/badges/version/epiteks/notifysms.svg)](https://microbadger.com/images/epiteks/notifysms)

🔔 ➡ 📱 Get Epitech notifications by SMS via Free Mobile

## How to use it ?

### Via Docker

Via CLI :

````bash
$> docker run -d -e "SMS_LOGIN=login" -e "SMS_TOKEN=token" -e "EPITECH_MAIL=mail" -e "EPITECH_PWD=pwd" epiteks/notifysms
````

Via Docker Compose :
````yaml
notifysms:
  image: epiteks/notifysms
  environment:
   - SMS_LOGIN
   - SMS_TOKEN
   - EPITECH_MAIL
   - EPITECH_PWD
  restart: always
````

### Local

You need to set these variables into your environment :
- NOTIFYSMS_DIR
- SMS_LOGIN
- SMS_TOKEN
- EPITECH_MAIL
- EPITECH_PWD

`NOTIFYSMS_DIR` is the location of `NotifySMS` directory.

`SMS_*` are used by [`freemobilesms`](https://github.com/hug33k/freemobilesms).
You can get these infos in your [Free Mobile panel](https://mobile.free.fr/moncompte/)

`EPITECH_*` are used to log you in via [our wrapper](https://github.com/epiteks/wrapitech).

Example :
````bash
export NOTIFYSMS_DIR=`pwd`
export SMS_LOGIN=xxxxxxx
export SMS_TOKEN=xxxxxxx
export EPITECH_MAIL=login_x@epitech.eu
export SMS_TOKEN=unix_pwd
````

Then you will need to install needed packages via [`pip`](https://pip.pypa.io/en/stable/installing/).

````bash
$> pip install -r requirements.txt
````

If you want to execute this program regularly, you can use cron.
Command is available in `crontab`[crontab].

````sh
$> crontab -l | cat - crontab | crontab -
````

This configuration will ask cron to execute `NotifySMS` every 2 minutes.
You can change it before execute this command.

## FAQ

#### What about other mobile network operators ?

Since I am using Free Mobile, I can't implement other services.

But feel free to contribute !

#### I can't login, what can I do ?

Unfortunately, we don't support OAuth with [Wrapitech](https://github.com/epiteks/wrapitech).

Once again, feel free to contribute !

#### What is `history.json` ? Can I delete it ?

This file is our "database". It stores the notifications you already got.

If you delete it, you will get a lot of messages next time you will run it.
