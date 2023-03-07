class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"ถ้าฝากเงิน = {amount} บาท ,ยอดเงินใหม่ = {self.balance} บาท")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"ถ้าถอนเงิน = {amount} บาท ,ยอดเงินใหม่ = {self.balance} บาท")
        else:
            print("Insufficient funds.")
            
    def display_balance(self):
        print(f"ยอดเงินในบัญชีสำหรับ {self.account_holder_name} เหลือ {self.balance} บาท")
        
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate
        
    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"ดอกเบี้ยที่ได้รับจากการฝาก =  {interest} บาท, ยอดเงินใหม่ = {self.balance} บาท")
account1 = BankAccount("555555555", "นพกร", 50000)
account1.deposit(2000)
account1.withdraw(1000)
account1.display_balance()

savings_account1 = SavingsAccount("999999999", "ภัทรนาคินทร์", 100000, 2)
savings_account1.deposit(10000)
savings_account1.calculate_interest()
savings_account1.withdraw(20000)
savings_account1.display_balance()
