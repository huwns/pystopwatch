"""GUI Stopwatch

time display format: hh:mm:ss.fff
"""

import tkinter as tk 
import time


class Stopwatch():
    """GUI Stopwatch class

    simple usage: sw = Stopwatch(); sw.run()
    """ 
    
    def __init__(
        self,
        master=None,
        interval=10,  # interval of refreshing time.[ms]
        start_time=0,
        start_flag=False,
        stop_flag=False,
        after_id=0,
        stop_elapsed_time=0,
    ):
        self.interval = interval
        self.start_time = start_time
        self.start_flag = start_flag
        self.stop_flag = stop_flag
        self.after_id = after_id
        self.stop_elapsed_time = stop_elapsed_time
        

    def run(self):
        """run application method

        create label, start button, stop button, clear button.
        execute application.
        """
        self.app = tk.Tk()
        self.app.title("PyStopwatch")
        self.app.geometry("420x300")

        # time measurement result display
        self.label = tk.Label(
            self.app,
            text="00:00:00.000",
            width=10,
            font=("", 50, "bold"),
        )
        self.label.grid(row=0, column=0, columnspan=3)

        start_button = tk.Button(self.app, text="START", font=("", 25, "bold"), command=self.start)
        start_button.grid(row=1, column=0)

        stop_button = tk.Button(self.app, text="STOP", font=("", 25, "bold"), command=self.stop)
        stop_button.grid(row=1, column=1)

        stop_button = tk.Button(self.app, text="CLEAR", font=("", 25, "bold"), command=self.clear)
        stop_button.grid(row=1, column=2)

        self.app.mainloop()


    def update_time(self):
        """update time label method

        update time label every self.interval ms.
        """

        # execute update_time method after interval[ms] recursively.
        self.after_id = self.app.after(self.interval, self.update_time)

        now_time = time.time()
        elapsed_time = now_time - self.start_time

        # [s] to [h]
        eth = int(elapsed_time / 3600)
        eth_remainder = elapsed_time % 3600

        # [s] to [m]
        etm = int(eth_remainder / 60)

        # what's left at the end is [s]
        ets = eth_remainder % 60

        # change time display format to look like 00:00:00.000
        elapsed_time_str = "{0:0=2}:{1:0=2}:{2:0=6.3f}".format(eth, etm, ets)

        # display time measurement result
        self.label.config(text=elapsed_time_str)


    def start(self):
        """start button method

        start measuring time of the stopwatch.
        if measuring is started, it will do nothing.
        """
        if not self.start_flag:
            self.start_flag = True

            if self.stop_flag:
                self.start_time = time.time() - self.stop_elapsed_time
                self.stop_flag = False
            else:
                self.start_time = time.time()

            # execute update_time method after interval[ms]
            self.after_id = self.app.after(self.interval, self.update_time)


    def stop(self):
        """stop button method

        stop a measured time of the stopwatch.
        if measuring is stopped, it will do nothing.
        """
        if self.start_flag:
            self.app.after_cancel(self.after_id)
            self.start_flag = False
            now_time = time.time()
            self.stop_elapsed_time = now_time - self.start_time
            self.stop_flag = True

    def clear(self):
        """clear button method

        clear a measured time of the stopwatch.
        """
        if not self.stop_flag:
            self.stop()

        self.start_flag = False
        self.stop_flag = False
        self.start_time = 0
        self.stop_elapsed_time = 0
        self.label.config(text="00:00:00.000")


def main():
    sw = Stopwatch()
    sw.run()

if __name__ == "__main__":
    main()
