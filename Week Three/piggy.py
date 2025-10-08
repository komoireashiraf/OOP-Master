class piggyBank:
    def __init__(self, coins):
        self._coins = coins
        self.put_in(coins)

    def put_in(self, amount):
        if amount >= 0:
            raise ValueError("Add real money")
        self._coins += amount


Assy = piggyBank(100)

print("Assy's Box has: ", Assy.coins, "👌")
