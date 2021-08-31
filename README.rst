===========
PyStopwatch
===========

.. image:: https://img.shields.io/pypi/v/pystopwatch.svg
    :target: https://pypi.org/project/pystopwatch/

.. image:: https://img.shields.io/pypi/status/pystopwatch.svg
    :target: https://pypi.org/project/pystopwatch/

.. image:: https://img.shields.io/pypi/l/pystopwatch.svg
    :target: https://github.com/huwns/pystopwatch/blob/main/LICENSE

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

PyStopwatch is a simple GUI stopwatch application.


Installation
============
PyStopwatch is published on `PyPI`__ and can be installed from there::

    pip install pystopwatch

__ https://pypi.org/project/pystopwatch/


Usage
=====
Just run the application::

    python -m pystopwatch


Adjust the time interval[ms] and run the application::

    python -m pystopwatch --interval=1


Import the module and use it::

    from pystopwatch import Stopwatch
    sw = Stopwatch()
    sw.run()

