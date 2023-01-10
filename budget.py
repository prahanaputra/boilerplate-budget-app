class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def __str__(self):
        title = self.name
        items = ""
        total = 0
       
        for item in self.ledger:
            items += f"{item['description']:<23.23s}{item['amount']:>7.2f}\n"
            total += item['amount']

        output = f"{title:*^30s}" + f"\n{items}" + f"Total: {total:<}"
        return output

    def get_balance(self):
        total_cash = 0

        for item in self.ledger:
            total_cash += item['amount']
        
        return total_cash
    

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -abs(amount), "description": description})
            return True
        else:
            return False
            
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False
            
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False
    
    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total

def create_spend_chart(categories):
    total_expense = 0
    expense_percent = []
    labels = []
    vertical_axis= [*range(100, -1, -10)]
    length_horizontal = len(categories)
    chart = ""
    chart_title = "Percentage spent by category\n"
    horizontal_axis = ""
    character = []

    for cat_1 in categories:
        total_expense +=  -1 * cat_1.get_withdrawals()

    for cat_2 in categories:
        percent = ((cat_2.get_withdrawals() / total_expense * 100 * -1) // 10) * 10
        expense_percent.append(percent)
    
    for cat_3 in categories:
        labels.append(cat_3.name)

    y = 100
    while y >= 0: 
        chart += f"{str(y):>3s}" + f"| "
        for n in expense_percent:
            if n >= y:
                chart += 'o  '
            else:
                chart += '   '
        chart += f"\n"
        y -= 10
    
    dash = f"    -" + f"{length_horizontal * '---'}" + f"\n"
    

    longest_label = len(max(labels, key=len))
    split_label = []
    for j in labels:
        split_label.append(list(j))
    
    c = 0
    while longest_label > c:
        horizontal_axis += f"     "
        for p in split_label:
            try:
                horizontal_axis += f"{p[c]}  "
            except IndexError:
                horizontal_axis += "   "
        if c < (longest_label - 1):
            horizontal_axis += "\n"
        else:
            pass
        c +=1

  

    
    output = chart_title + chart + dash + horizontal_axis
    return output