.. index:: Usage

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
