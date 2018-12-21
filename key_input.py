""""input from player"""

from __future__ import print_function
import signal

class AlarmException(Exception):
    """alarm"""
    pass


class GetchUnix(object):
    """get input"""
    def __init__(self):
        """inint"""
    def __call__(self):
        """"call"""
        import sys
        import tty
        import termios
        fd_1 = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd_1)
        try:
            tty.setraw(sys.stdin.fileno())
            ch_1 = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd_1, termios.TCSADRAIN, old_settings)
        return ch_1


GETCH = GetchUnix()


def alarm_handler(signum, frames):
    """"handle alarm"""
    raise AlarmException


def input_to(timeout=0.38):
    """input"""
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = GETCH()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
