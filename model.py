import time

class SilentThreatModel:
    def __init__(self):
        self.last_activity = time.time()
        self.risk_score = 0

    def register_activity(self):
        self.last_activity = time.time()
        self.risk_score = max(0, self.risk_score - 1)

    def evaluate(self):
        gap = time.time() - self.last_activity

        if gap < 5:
            return "GREEN", "Normal activity detected"

        elif gap < 12:
            self.risk_score += 1
            return "YELLOW", "Suspicious delay in activity"

        else:
            self.risk_score += 2
            return "RED", "Silent threat detected"
