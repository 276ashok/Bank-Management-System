class rbi():
    def __init__(self):
        self.tot_rbi_acc = 100
        self.tot_rbi_fund = 100000
        super().__init__()

class sbi(rbi):
    def __init__(self):
        self.tot_sbi_acc = 75
        self.tot_sbi_fund = 85000
        super().__init__()

class tn(sbi):
    def __init__(self):
        self.tot_tn_acc = 65
        self.tot_tn_fund = 70000
        super().__init__()

class kadayanallur(tn):
    def __init__(self):
        self.tot_kdnl_acc = 50
        self.tot_kdnl_fund = 50000
        super().__init__()

    def deposit_money(self, deposit):
        self.deposit = deposit
        self.tot_kdnl_fund += deposit
        self.tot_tn_fund += deposit
        self.tot_sbi_fund += deposit
        self.tot_rbi_fund += deposit
        print(f"Amount {deposit} deposit to this branch successfully")
        print(f"The Kadayanallur total fund is : {self.tot_kdnl_fund}")
        print(f"The Tamil Nadu total fund is : {self.tot_tn_fund}")
        print(f"The SBI total fund is : {self.tot_sbi_fund}")
        print(f"The RBI total fund is : {self.tot_rbi_fund}")

    def withdrawl_money(self, withdrawal):
        self.withdrawl = withdrawal
        self.tot_kdnl_fund -= withdrawal
        self.tot_tn_fund -= withdrawal
        self.tot_sbi_fund -= withdrawal
        self.tot_rbi_fund -= withdrawal
        print(f"Amount {withdrawal} withdrawl Successfully this branch")
        print(f"The Kadayanallur total fund is : {self.tot_kdnl_fund}")
        print(f"The Tamil Nadu total fund is : {self.tot_tn_fund}")
        print(f"The SBI total fund is : {self.tot_sbi_fund}")
        print(f"The RBI total fund is : {self.tot_rbi_fund}")

    def account_opening(self, new_acc_open):
        self.new_acc_open = new_acc_open
        self.tot_kdnl_acc += new_acc_open
        self.tot_tn_acc += new_acc_open
        self.tot_sbi_acc += new_acc_open
        self.tot_rbi_acc += new_acc_open
        print(f"The Kadayanallur total account is : {self.tot_kdnl_acc}")
        print(f"The Tamil Nadu total account is : {self.tot_tn_acc}")
        print(f"The SBI total account is : {self.tot_sbi_acc}")
        print(f"The RBI total account is : {self.tot_rbi_acc}")

    def account_closing(self, acc_close):
        self.acc_close = acc_close
        self.tot_kdnl_acc -= acc_close
        self.tot_tn_acc -= acc_close
        self.tot_sbi_acc -= acc_close
        self.tot_rbi_acc -= acc_close
        print(f"The Kadayanallur total account is : {self.tot_kdnl_acc}")
        print(f"The Tamil Nadu total account is : {self.tot_tn_acc}")
        print(f"The SBI total account is : {self.tot_sbi_acc}")
        print(f"The RBI total account is : {self.tot_rbi_acc}")


def account_opening():
    name=input("Enter a Name : ")
    age=int(input("Enter a Age : "))
    ph=int(input("Enter a Phone Number : "))
    print(f"Account open succeesfully for {name}")

def account_closing():
    name=input("Enter a Name : ")
    acc_no=int(input("Enter a account number : "))
    ph=int(input("Enter a Phone Number : "))
    print(f"Account close successfully for {name}")

obj = kadayanallur()

print("********** Kadayanallur Branch **********")
print("\n********** Please choose a service **********")
print("\n1. Withdrawl \n2. Deposit \n3. Account Opening \n4. Account Closing")

try:
    user=int(input("\nPlesae enter a number : "))
    if user==1:
        how_much=int(input("How much do you withdrawl : "))
        obj.withdrawl_money(how_much)
    elif user==2:
        how_much=int(input("How much do you deposit : "))
        obj.deposit_money(how_much)
    elif user==3:
        account_opening()
    elif user==4:
        account_closing()
    
except:
    print("\nEnter number only")
