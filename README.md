Detanglement
============

This repo contains a research project I work on at FKI/HTW Berlin.
As with most of my repositories, this is a work-in-progress, more specifically,
an alpha.

It is a tool that visualizes big amounts of geolocalized data on-demand.
At the moment, only a proof-of-concept plugin for WorldBanks' Indicator API
is working with it, but it can theoretically be extended to work with many
different APIs; that is the goal, anyway.

Requirements
------------

The tool requires a few additional python libraries to work, namely:

```
PyQt5
pygeoip
geopy
```

Additionally, if you want the WorldBank plugin to work(which is the
only working plugin right now, so you might), you need to install
`wbpy`.
Also, if you want to check out the nonworking plugin for Twitter(which
adds markers to the map, but the data is not visualized), you need
to install `TwitterAPI`.

I have included all Javascript APIs you might need, hoping that no
licensing issues will emerge.

Usage
-----

There are many ways to invoke/use the application. I suggest you `git clone`
the repository first, change into the `src`directory and check out the 
command-line features(by invoking `./Tangle.py -h`). To wrap up what I 
just told you, it should look like this:

```bash
git clone https://github.com/hellerve/Detanglement.git
cd Detanglement/src
./Tangle.py -h
```

After you have made yourself familiar with the main scripts' features, you 
can explore the tool by typing:

```bash
./Tangle.py -f
./Tangle.py -a WorldBank
```

Which loads the script with WorldBanks' Indicator API and shows the tools
capabilities pretty well. Click around, make yourself at home.

![This is what you should see](https://github.com/hellerve/Detanglement/tree/master/rc/Documentation/startup.png, "This is what you should see")

![Geolocation](https://github.com/hellerve/Detanglement/tree/master/rc/Documentation/geolocation.png, "If you want it to, the tool, even geolocalizes you!")

Sooner or later you will want to visualize something, because, you know,
that is what the tool is about. You can click any marker; a window will pop
open and ask you to apply filters. 

![You will be greeted by this window](https://github.com/hellerve/Detanglement/tree/master/rc/Documentation/filter.png, "You will be greeted by this window")

Certain filters will not be available for certain
areas, but you will see that by experimenting. Other filters(like `Population
(Total)`) will almost always be available. You can fiddle around, search them
by the search bar or by hand(but that might be pretty unconformtable, because
WorldBank provides well over 9000(no pun intended) filters. You can also supply it
regular expressions. If those are not valid, it will try to search it literally.

![Regexes! Yay!](https://github.com/hellerve/Detanglement/tree/master/rc/Documentation/regex.png, "Regexes! Yay!")

Sooner or later you will find the filters you want to apply: Dragging them into
the second(empty) list will select them and if you click apply, a different window
should open and visualize the filters for you - except if you get a notification that
the filter did not provide any data.

![Score! Visuals!](https://github.com/hellerve/Detanglement/raw/master/rc/Documentation/visuals.png "Score! Visuals")

If you click the settings icon(the little cogwheel in the toolbar), you will also
have the possibility to select an alternative map(Kartograph is not working right now,
because it is based on Python 2.7 and we are using Python 3+, but we are working
on that). You can also toggle geolocation and APIs, although the API section should look
a bit... empty.

Well, that's it with the features. There is more to come, though, so be prepared!


Writing Plugins
---------------

Coming soon.

Contribute
----------

What needs to be done? Well, many things. I documented most of the bugs in a file
in `rc` called `KNOWN_BUGS`. You can add to it or open an issue. There is also file
in the directory called `PLANNED_FEATURES`, documenting what needs to be done.
You can also look at both files by invoking `./Tangle.py -d` or `./Tangle.py --devel`
or, if you have installed it (kudos, you are likely to use Linux, because it is a pain
to install it on any other platform at the moment) `Tangle -d`.

The feature I am currently working on is a GUI frontend for the database so you can
conveniently add new APIs and API keys to the application. A database wrapper needs
to be created sooner or later as well(as it stands, the only database code is inlined
into a definition in the main script; not very beautiful).

Also, the help file is a mess that needs to be cleaned up by someone who enjoys writing
HTML files more than me. It is a non-informative mess.

I suggest you code a plugin and see if it works. If it does not, we can look at what is
the problem and fix it together.
