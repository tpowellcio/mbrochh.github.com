Date: 2012-04-21
Title: Snippets of April 2012
Slug: snippets-201204
Category: Blog
Tags: snippets
status: draft

This is my second post in a series of (almost) monthly posts about small bits
and pieces of wisdom that amazed me. You can find the first post here:
[Snippets of February 2012](http://martinbrochhaus.com/2012/02/snippets-201202.html)


# Ubuntu: Static Application Switcher

App switiching with ALT+TAB became a major pain since Ubuntu introduced that
horrible Unity interface. The simple solution is to open CompizConfig Settings
Manager and enable "Static Application Switcher" under "Window Management".

I think it is much much more intuitive and effective to have a static list of
windows instead of an endlessly rotating one.

# Scrolling, Copy & Paste in GNU Screen

I really got to love screen during the past 4 months and usually work in a
session with 7 windows open. The problem is, when I swtich to window 1 to see
the output of my tests and there is a huge traceback, I cannot use my terminal
to scroll up because I will scroll into whatever I saw in the windows before
(probably Vim).

The trick is to use Screen's scroll mode by pressing ``CTRL+A ESC``. It will
display a message saying that copy mode is activated and now you can move the
cursor with the usual Vim keybindings. Pressing ``SPACE`` or ``ENTER`` once
sets a marker and pressing it again will copy everything between the first and
second marker into the clipboard.

You can paste the clipboard via ``CTRL+A ]``. Yea, I know. Read the fucking
manual... :)

# SSH Keep Alive

Whenever I need to SSH into my various servers I get connection timeouts all
the time. Somehow most people don't suffer from this so this seems to be a
problem with my Ubuntu installation, but recently I found a solution that works
for me:

On my servers, I now set this:

    ::text
    # in ~/.ssh/config:
    ServerAliveInterval 60

    ::text
    # in ~/.screenrc
    caption always '%c:%s'

Now I just need to remember to start a screen session right after I login. The
screen setting will render a clock at the bottom of the screen which is enough
to have a steady bit of traffic going through SSH for not kicking me out of the
server any more.

# Nerdy IT Jargon

I can't remember where I learned about these but I love them:

* ``<=>`` is called the spaceship operator
* Writing variable names ``LikeThis`` is called CamelCase. I knew this for
  years, but:
* Writing variable names ``like_this`` is called ``snake_case``. Very Pythonic,
  isn't it?

# HG Facepalm

I can't believe that this actually happened, but if you have something from
Bitbucket in your requirements.txt and try to pip install it, you might get
a weird error saying that the pip call to Bitbucket returned code 1 and this
pip stops installing.

This is because a recent version of Mercurial returns 1 if ``hg pull`` doesn't
return any new changes (which happens most of the time).

However, pip (and almost every other software on this planet) thinks that a
return value of 1 means a failure and just stops.

Thankfully Mercurial fixed this quickly and reverted that change, so if you are
suffering from the "bad" version, you might want to upgrade your Mercurial
installation.

* [Mercurial upgrade notes](http://mercurial.selenic.com/wiki/UpgradeNotes)
* [Relevant GitHub issue for pip](https://github.com/pypa/pip/issues/454)

# Great blog posts

* http://www.dailygood.org/view.php?sid=194
* http://www.stumbleupon.com/su/9IbGnD/zenhabits.net/the-only-guide-to-happiness-youll-ever-need/
* http://carl.flax.ie/dothingstellpeople.html
* http://steve-yegge.blogspot.com/2006/09/good-agile-bad-agile_27.html

# git aliases

# git defaults
http://jk.gs/git-config.html

    [push]
        default = upstream

# factory_boy
# access django from parallels

    ::sh
    ifconfig -a
    ./manage.py runserver 192.168.0.10:8000

In Parallels, start IE and browse to http://192.168.0.10:8000

# Chinese translations in Django

http://stackoverflow.com/questions/7728977/django-how-to-add-chinese-support-to-the-application

Put ``zh-cn`` in your settings.py but run ``makemessages -l zh_CN``


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



