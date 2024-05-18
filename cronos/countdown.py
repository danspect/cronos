import threading
import time


class Countdown:
    def __init__(self) -> None:
        # Cda valor corresponde a:
        # [1min, 2min, 3min, 5min, 15min, 30min, 45min and 1 hour].
        # self.default_values = [60, 120, 180, 300, 900, 1800, 2700, 3600]
        self.remaining_time = 0
        self._paused = True
        self._reset = False
        self.timer_thread = None

    def start(self, time_sec) -> None:
        self.remaining_time = time_sec
        self._paused = False
        self._reset = False
        if self.timer_thread == None or not self.timer_thread.is_alive():
            self.timer_thread = threading.Thread(target=self._run)
            self.timer_thread.start()

    def pause(self) -> None:
        self._paused = True

    def reset(self) -> None:
        self._paused = True
        self._reset = True
        self.remaining_time = 0

    def get_remaining_time(self) -> int:
        return self.remaining_time

    def add_one_minute(self) -> None:
        self.remaining_time += 60

    def _run(self) -> None:
        while self.remaining_time > 0 and not self.reset:
            if not self._paused:
                time.sleep(1)
                self.remaining_time -= 1
            else:
                time.sleep(0.1)

        if self.remaining_time <= 0:
            self.reset()
