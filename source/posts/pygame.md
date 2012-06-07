Date: 2012-06-07
Title: PyCon APAC 2012 - Introduction to game development
Slug: pygame
Category: Blog
Tags: python, pycon, conferences
status: draft

Richard Jones is holding the 3.5 hours tutorial session.
22 people are here at 9:15am but I guess more will drop in being late.

We got a .zip file with a whole game inside. Richard was nice enough to put it
into public domain, so we can tinker with it and build upon it.

Richard asks who never wrote any Python code. No one raises hands.

# Display Something

* We can display images, draw primitives, draw fonts or use OpenGL.
* Not going to cover OpenGL today, unfortunately.

A first pygame program is really simple:

    ::py
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480))


Better put some structure to your code. Create a Game() class with a main()
method. Don't use global variables.

In pygame, unlike in modern frameworks, the coordinate ``0,0`` is the top left
corner. This is because video hardware draws like this. More modern systems
like OpenGL separate the drawing part from the display part so that we can use
a more sane coordinate system with ``0,0`` at bottom left.

Let's draw something:

    ::py
    image = pygame.image.load('player.png')
    screen.fill((200, 200, 200))  # Fill the screen with a background color
    screen.blit(image, (320, 240))  # Copies the image to that position on screen 
    pygame.display.flip()

Pygame uses RGB colors.

We learn about "tearing". If we draw to the screen directly, the screen might
refresh while we change what is on the screen so we will see something in
between. So we must use ``display.flip()`` at the end of our drawing.

Via ``pygame.tick.Clock()`` we can put the main loop to sleep. 30 FPS should
be a good frame rate for any video game.

Our first animation is just adding 10 pixels to the image position.

Side effect of double buffering: When we ``clear`` the old buffer will remain.
Therefore if we would not re-render the background image all the time, our
character would appear to have a trail when moving.

# User input

Pygame can tell us which keys are currently pressed, as opposed to inform us
about key down events:

    ::py
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        image_x -= 10

# Sprites

To put things together, we can define sprites, which are images, that know how
they look like and where they are on screen. We can give them an ``update``
method and handle their user input.

    ::py
    class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('player.png')
        self.rect = pygame.rect.Rect((320, 240), self.image.get_size())

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 10

You would want to pass the amount of time that has passed since the last loop
call and pass it into the update method. Then don't just jump 10 pixels but
multiply the passed time with a value.

# Collision detection

Axis-Aligned bounding box is the most common collision detection. The name says
it all, think about it.

An alternative would be to use circles as bounding boxes.

A third alternatives is to use a hash map, which is useful for 2D games with
thousands of sprite on screen. This is usually used for so called ``Bullet
Hell`` games. Didn't know about this term before :)

You could finally do pixel perfect collision detection but that might be quite
slow.

# Tile maps

.tmx is a common format for tile maps that make up the game world.  It has an
editor called ``Tiled`` which you can get at
[mapeditor.org](http://mapeditor.org) You can kind of paint the map of that
level. The tile map also as a layer or trigger tiles which can be trigger
events. Pygame knows how to read those .tmx files and can access the triggers.

The player only sees a fraction of the whole tile map. This is called the view
port.


From here on it is pretty much all about doing lots of if and else clauses
reacting to collisions and inputs. It seems to me that the hardest part about
game development is structuring your code as efficient as possible because it
can quickly grow into a huge amount of spaghetti code.

# Sound

As expected, adding sound is extremely easy as well:

    ::py
    self.jump = pygame.mixer.Sound('jump.wav')
    self.jump.play()

[SFXR](https://code.google.com/p/sfxr/) is a great little tool that emulates
the sound chip of the C64 and allows you to model cute 8bit sounds for your
game.

# Special effects

You can use ``pip install lepton``, a library for particles. Richard repeats:
"Every single game improves with particles" :) He mentions a talk called
[Juice it or lose it](https://www.youtube.com/watch?v=Fy0aCDmgnxg) which is
about techniques to juice up your game with special effects.

# Where to go from here

[pygame.org](http://pygame.org)
[inventwithpython](http://inventwithpython.com)
[pyweek.org](http://pyweek.org)

# Tools

* [mapeditor.org](http://mapeditor.org) - Creates tile maps
* [SFXR](https://code.google.com/p/sfxr/) - Creates sound files
* [Pyxel Edit](http://danikgames.com/stuff/pyxeledit/) - Creates seamless
  tiles.
* [Pixen](http://pixenapp.com/) - Creates moving animatinos for characters
* [cocos2d.org](http://cocos2d.org/doc.html) - Helps with adding juice

? How to do path finding for a point and click adventure game?
? How to bundle and ship the game?

