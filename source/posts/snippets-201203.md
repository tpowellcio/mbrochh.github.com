Date: 2012-03-31
Title: Snippets of March 2012
Slug: snippets-201203
Category: Blog
Tags: snippets
status: draft

Naturally, as a developer I learn new awesome things almost every day.
I thought it might be a good idea to keep track of all those small Ah-Ha!
moments and release a snippets post every month.

# factory_boy

# Static Application Switcher
* open CompizConfig Settings Manager
* Disable AppSwitcher
* Enable static app switcher

# scrolling, copy and paste in screen

* C-A ESC enters copy mode, here I can scroll the real scrollback buffer
* Space sets first marker, enter copies lines
* C-A ] pastes text


# git aliases

# git defaults
http://jk.gs/git-config.html

    [push]
        default = upstream

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

# Replacing a field on a form

Let's assume:

    ::py
    class FooBar(models.Model):
        foo = models.IntegerField()
        bar = models.IntegerField()

    class FormBar(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(FormBar, self).__init__(*args, **kwargs)
            self.fields['bar'] = MyCustomIntegerField()

    class FormFooBar(FormBar):
        class Meta:
            model = FooBar

Usually we would instantiate the form ``FormFooBar`` which gets all it's fields
created by the model. However, in the superclass, ``FormBar`` we would like
to replace the automatically created field ``bar`` by a custom implementation
of the IntegerField which would display a different value than the one that
is actually saved on the instance.

The code above would still show the value from the instance. It took me quite
some time to find out that we also need to add this line after:

    ::py
    ...
    self.fields['bar'] = MyCustomIntegerField()
    self.initial['bar'] = my_custom_calue

# HG Facepalm
* http://mercurial.selenic.com/wiki/UpgradeNotes
* https://github.com/pypa/pip/issues/454

# Django and Sphinx autodoc
* add the following to conf.py

    ::py
    sys.path.insert(0, os.path.abspath('../website/webapps/django/'))
    # setup django
    import settings
    from django.core.management import setup_environ
    setup_environ(settings)

* change this in Makefile

    ::sh
    SPHINXBUILD   = python $(shell which sphinx-build)

* run sphinx-apidoc -f -o api ../website/webapps/django/project

# django-cms dumpdata placeholder

* do not name your placeholders '01 content', better '01_content'


# Great blog posts

* http://carl.flax.ie/dothingstellpeople.html
* http://steve-yegge.blogspot.com/2006/09/good-agile-bad-agile_27.html
* http://www.dailygood.org/view.php?sid=194
* http://www.stumbleupon.com/su/9IbGnD/zenhabits.net/the-only-guide-to-happiness-youll-ever-need/
