"""CUI Executer"""

import argparse

from pystopwatch import Stopwatch


def main():
    parser = argparse.ArgumentParser(
        description=r"""PyStopwatch - Simple GUI Stopwatch
+----------------------------------------------------------------------------------+
|__________         _________ __                                __         .__     |
|\______   \___.__./   _____//  |_  ____ ________  _  _______ _/  |_  ____ |  |__  |
| |     ___<   |  |\_____  \\   __\/  _ \\____ \ \/ \/ /\__  \\   __\/ ___\|  |  \ |
| |    |    \___  |/        \|  | (  <_> )  |_> >     /  / __ \|  | \  \___|   Y  \|
| |____|    / ____/_______  /|__|  \____/|   __/ \/\_/  (____  /__|  \___  >___|  /|
|           \/            \/             |__|                \/          \/     \/ |
+----------------------------------------------------------------------------------+""",
        prog="python -m pystopwatch",
        formatter_class=argparse.RawDescriptionHelpFormatter,
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
