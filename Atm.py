class atm:
    def __init__(self, card_number, pin, balance):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
    
    def check_balance(self):
        print("your balance is", self.balance)

    def cash_withdrawel(self):
      #  print("your withdrawed $100, your balance now is", self.balance)
      print("your balance now is", cash_withdrawel)
    def balance_enquiry(self):
        print(balance_enquiry)

balance_enquiry = "You have free health insurance with this card!"

card_number = input("what is your card number?")
pin_number = input("what is your pin number?")
balance = input("what is your balance?")

cash_withdrawel = int(balance) - 100

new_user = atm(card_number, pin_number, balance)

user_choice = int(input("Type 1 to see your balance enquiery\nType 2 to withdraw $100 from your balance\nType 3 to check your balance\n"))
if user_choice == 1:
    print(new_user.balance_enquiry())
elif user_choice == 2:
    print(new_user.cash_withdrawel())
elif user_choice == 3:
    print(new_user.check_balance())
else:
    print("Please run the code again, somthing went wrong")
