"""CUI Executer"""

import argparse

from pystopwatch import Stopwatch


def main():
    parser = argparse.ArgumentParser(
        description="PyStopwatch", prog="python -m pystopwatch"
    )
    parser.add_argument("--interval", help="interval of refreshing time.[ms]", type=int)
    args = parser.parse_args()
    if args.interval:
        sw = Stopwatch(interval=args.interval)
    else:
        sw = Stopwatch()
    sw.run()


if __name__ == "__main__":
    main()
