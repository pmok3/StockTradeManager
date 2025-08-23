class FSM:
    def __init__(self, ticker, start, end, win, lose, debug):
        self.ticker = ticker
        self.start_state = start
        self.end_state = end
        self.win_state = win 
        self.lose_state = lose
        self.debug_messages = debug
        self.curr_state = start
    
    def eval_state(self, ticker):
        pass
