import time


class Cronometer:
    def __init__(self) -> None:
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

    def start(self) -> None:
        if not self.running:
            self.running = True
            self.start_time = time.time()

    def pause(self) -> None:
        if self.running:
            self.running = False
            self.elapsed_time += time.time() - self.start_time

    def reset(self) -> None:
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

    def get_time(self) -> int:
        if self.running:
            return self.elapsed_time + time.time() - self.start_time
        else:
            return self.elapsed_time
