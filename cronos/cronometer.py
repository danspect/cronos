import time

class cronometer():
    def __init__(self) -> None:
        self.running = False
        self.start_time = 0
        self.elapsed_time = time.time() - self.start_time
    
    def start(self) -> None:
        if not self.running:
            self.running = True
            self.start_time = time.time()
    
    def pause(self) ->None:
        pass
    
    def reset(self) -> None:
        self.running = False
        self.start_time = 0

    def get_time(self) -> int:
        return self.elapsed_time