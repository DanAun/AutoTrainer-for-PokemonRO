class BattleTimeoutError(Exception):
    def __init__(self, message="Battle took too long to finish"):
        self.message = message
        super().__init__(self.message)


class NotInBattleError(Exception):
    def __init__(self, message="Is not in battle"):
        self.message = message
        super().__init__(self.message)
