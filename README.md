# Description

**BonusDesk** is a  commercial project developed for "EnjoyJumping" fitness organization. A referral bonus system was implemented in the current project.

# Implementation detail

`Django` web framework (version 1.11.5) and `Python` programming language (version 3.6) were used to create the current project. `PostgreSQL` had been used as a DBMS.

`Celery + Redis` were used to execute periodic asynchronous tasks in a Django project.

The project uses several third-party packages which you can install to your virtual environment by command:

```pip install -r requirements.txt```

In that project we used `Yandex Metrika` to measure website traffic and analyze user behavior.

# How it works?

System redirect user to his personal dashboard after successfull registration.

![](https://github.com/NogerbekNurzhan/BonusDesk/blob/master/screenshots/9.png)

When user first log in website, he will see his referral link and small message about his payment status.

![](https://github.com/NogerbekNurzhan/BonusDesk/blob/master/screenshots/5.png)

![](https://github.com/NogerbekNurzhan/BonusDesk/blob/master/screenshots/4.png)

The administrator changes the status of payment after buying a subscription to the fitness room for month by that user.

![](https://github.com/NogerbekNurzhan/BonusDesk/blob/master/screenshots/6.PNG)

After that user can see all information about accumulation in each level of referral system. `django-mptt` was used to store hierarchical data. In frontend we use `nestable` library to show  hierarchical tree of followers.

User also can set his parent later if he did not come to the website by referral link of his friend.

![](https://github.com/NogerbekNurzhan/BonusDesk/blob/master/screenshots/8.png)

![](https://github.com/NogerbekNurzhan/BonusDesk/blob/master/screenshots/7.png)

The administrator of the system can see information of any user he want in dashboard page. He just need to enter username of that user to autocomplete field of next form:

![](https://github.com/NogerbekNurzhan/BonusDesk/blob/master/screenshots/10.png)

More information about implementation of referral bonus system you can find in [views.py](https://github.com/NogerbekNurzhan/BonusDesk/blob/master/dashboard/views.py) file of **dashboard** application.
