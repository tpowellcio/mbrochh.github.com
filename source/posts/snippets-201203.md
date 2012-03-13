Date: 2012-03-31
Title: Snippets of March 2012
Slug: snippets-201203
Category: Blog
Tags: snippets
status: draft

Naturally, as a developer I learn new awesome things almost every day.
I thought it might be a good idea to keep track of all those small Ah-Ha!
moments and release a snippets post every month.

# git aliases

# access django from parallels

    ::sh
    ifconfig -a
    ./manage.py runserver 192.168.0.10:8000

In Parallels, start IE and browse to http://192.168.0.10:8000

# Chinese translations in Django

http://stackoverflow.com/questions/7728977/django-how-to-add-chinese-support-to-the-application

Put ``zh-cn`` in your settings.py but run ``makemessages -l zh_CN``

# Jargon

* <=> The spaceship operator
* CamelCase vs. ``snake_case``

# ssh keep alive

In ~/.ssh/config:

    ::text
    ServerAliveInterval 60

In ~/.screenrc

    ::text
    caption always '%c:%s'
