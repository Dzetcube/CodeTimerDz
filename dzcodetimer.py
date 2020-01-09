"""
Dz CodeTimer
a 'code run' timer

by Dzikri Fudholi 2020
"""
import time


class CodeTimer:
    """
    Timer Object
    to store :
     - overall start time
     - step start time
    to display :
     - seconds of elapsed time from start
     - seconds of elapsed time from the start of step
    """
    def __init__(self):
        self.start_time = time.time()

    def check(self, comment='-'):
        """
        Print seconds of elapsed time from start and return them

        :param comment: String
        :return: int: Elapsed Second(s)
        """
        elapsed_time = time.time() - self.start_time

        print("step :", comment)
        print("elapsed time :", elapsed_time, 'seconds')

        return elapsed_time

    def start_step(self):
        """
        Setting the start time of a step.
        To be used before every end_step

        :return: True
        """
        self.start_step_time = time.time()
        return True

    def end_step(self, comment='-'):
        """
        Print seconds of elapsed time from the start of step

        :param comment: String
        :return: Elapsed Second(s)
        """
        elapsed_time = time.time() - self.start_step_time

        print("step :", comment)
        print("runs :", elapsed_time, 'seconds')

        return elapsed_time

