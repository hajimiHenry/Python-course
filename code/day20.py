class Man:
    def __init__(self, name, identity):
        self.name = name
        self.id = identity

    def print_info(self):
        print(f"员工的姓名是{self.name}id是{self.id}")


class FullTimeEmployee(Man):
    def __init__(self, name, identity, monthly_salary):
        super().__init__(name, identity)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Man):
    def __init__(self, name, identity, daily_salary, work_days):
        super().__init__(name, identity)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days


Henry = FullTimeEmployee("张三", "1001", 6000)
Jack= PartTimeEmployee("李四", "1002", 600, 30)


Henry.print_info()
Jack.calculate_monthly_pay()
print(Henry.calculate_monthly_pay())
print(Jack.calculate_monthly_pay())
