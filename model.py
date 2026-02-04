import time

class SilentThreatModel:
    def __init__(self):
        self.last_activity = time.time()

    def predict(self):
        idle_time = time.time() - self.last_activity

        if idle_time < 5:
            return "GREEN", "Normal activity detected"

        elif idle_time < 15:
            return "YELLOW", "Suspicious inactivity"

        else:
            return "RED", "Silent threat detected"
