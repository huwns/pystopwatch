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

.. image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

PyStopwatch is a simple GUI stopwatch application.


Installation
============
PyStopwatch is published on `PyPI`__ and can be installed from there::

    pip install pystopwatch

__ https://pypi.org/project/pystopwatch/


Usage
=====
To get started right away, run the following command::

    pystopwatch


You can run PyStopwatch as a package if running it as a script doesn't work::

    python -m pystopwatch


Adjust the time interval[ms] and run the application::

    pystopwatch --interval=1


Import the module and use it::

    from pystopwatch import Stopwatch
    sw = Stopwatch()
    sw.run()
