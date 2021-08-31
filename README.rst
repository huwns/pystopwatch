===========
PyStopwatch
===========
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
    import pystopwatch
    sw = pystopwatch()
    sw.run()
