
import coinbase

class Monitor():
    def __init__(self, trader, sell_threshold, buy_threshold):
        self.trader = trader
        self.buy_thresh = buy_threshold
        self.sell_thresh = sell_threshold

    def check_profit(self):
        """ check_profit = (amount * sell price) > fees*10 """

