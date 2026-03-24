class trade_value:
    def __init__ (self, name, value, sold):
        self.name = name
        self.value = value
        self.sold = sold

#Source for now is only meant to be used as the inventory, in the future i'll add another sources to keep the money and trade with it.

def trading(source, trade_item):
    if source["Gold"] < trade_item.value:
        print ("You don't have enough money.")
        return
    else:        
        source["Gold"] -= trade_item.value
        source[trade_item.name] = 1
        print (f"Trade complete!\nYou bought: {trade_item.name}")
        trade_item.sold = True

Room_key = trade_value("Room key", 50, False)           