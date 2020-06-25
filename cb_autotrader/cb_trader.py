
import .cb_auth

class CB_Trader():
    API_URL = 'https://api.coinbase.com/v2'

    def __init__(self, api_key, api_secret):
        self.auth = cb_auth.CoinbaseWalletAuth(api_key, api_secret)
        self.client = coinbase.wallent.client(api_key, api_secret)

    def get_transaction_fee(self, amt):
        # Prices in USD
        # Fee rates from Coinbase website
        if amt <= 10:
            return 0.99
        elif amt <= 25:
            return 1.49
        elif amt <= 50:
            return 1.99
        elif amt <= 200:
            return 2.99
        else:
            # Rates based off of percentage
            return 10

    def buy_price(self, coin, currency):
        return client.get_buy_price('-'.join(coin, currency))

    def sell_price(self, coin, currency):
        return client.get_sell_price('-'.join(coin, currency))


