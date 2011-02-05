media-guid.org
==============
This is a community site intended to register one unique ID for each unique
work (e.g., movie, TV show/series, written publication, painting), or any
media-related entity (e.g., author, musical group, publisher), and link it to
any associated media-guid, ISBN/ASIN, websites, etc.

Installation and Setup
======================

Install ``media-guid`` using the setup.py script::

    $ cd media-guid
    $ python setup.py install

Create the project database for any model classes defined::

    $ paster setup-app development.ini

Start the paste http server::

    $ paster serve development.ini

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ paster serve --reload development.ini

Then you are ready to go.
