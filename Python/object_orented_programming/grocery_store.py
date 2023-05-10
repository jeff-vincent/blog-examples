class GroceryStore:
    def __init__(self):
        self.items = [{'name':'milk', 'count': 10}, {'name': 'bread', 'count': 20}, {'name': 'eggs', 'count': 10}]

    def add_item(self, item):
        self.items.append(item)

    def add_inventory(self, stock):
        for item in self.items:
            if stock['name'] == item['name']:
                item['count'] += stock['count']
            else:
                self.items.append(stock)
    
    def sell_item(self, purchased_item):
        for item in self.items:
            if purchased_item['name'] == item['name']:
                item['count'] = item['count'] - 1
                if item['count'] == 0:
                    self.items.remove(item)
