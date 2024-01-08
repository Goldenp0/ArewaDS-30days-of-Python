class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

    def mode(self):
        counts = {value: self.data.count(value) for value in set(self.data)}
        max_count = max(counts.values())
        mode_values = [key for key, value in counts.items() if value == max_count]
        return {"mode": mode_values[0], "count": max_count}

    def std(self):
        mean = self.mean()
        squared_diff = sum((x - mean) ** 2 for x in self.data)
        variance = squared_diff / (len(self.data) - 1)
        return variance ** 0.5

    def var(self):
        mean = self.mean()
        squared_diff = sum((x - mean) ** 2 for x in self.data)
        return squared_diff / (len(self.data) - 1)

    def freq_dist(self):
        unique_values = list(set(self.data))
        freq_distribution = [(self.data.count(value), value) for value in unique_values]
        return sorted(freq_distribution, reverse=True)

    def describe(self):
        result = f"Count: {self.count()}\n"
        result += f"Sum: {self.sum()}\n"
        result += f"Min: {self.min()}\n"
        result += f"Max: {self.max()}\n"
        result += f"Range: {self.range()}\n"
        result += f"Mean: {self.mean()}\n"
        result += f"Median: {self.median()}\n"
        result += f"Mode: {self.mode()}\n"
        result += f"Variance: {self.var()}\n"
        result += f"Standard Deviation: {self.std()}\n"
        result += f"Frequency Distribution: {self.freq_dist()}"
        return result


class PersonAccount:
    def __init__(self, firstname, lastname, incomes=None, expenses=None):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes if incomes else {}
        self.expenses = expenses if expenses else {}

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        return f"{self.firstname} {self.lastname}'s Account:\n" \
               f"Total Income: {self.total_income()}\n" \
               f"Total Expense: {self.total_expense()}\n" \
               f"Account Balance: {self.account_balance()}"

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def account_balance(self):
        return self.total_income() - self.total_expense()
        
# Example usage for Statistics class
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.describe())

# Example usage for PersonAccount class
person = PersonAccount("John", "Doe", incomes={"Salary": 5000, "Bonus": 1000}, expenses={"Rent": 1500, "Groceries": 500})
print(person.account_info())
person.add_income("Freelance Work", 800)
person.add_expense("Utilities", 200)
print(person.account_info())




