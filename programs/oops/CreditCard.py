# Program to demonstrate Credit Card application 

import random as rd

class BasicInfo():
    def __init__(self, f_name, l_name, age: int, city, state):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age 
        self.city = city 
        self.state = state

class FinancialInfo(BasicInfo):
    def __init__(self, f_name, l_name, age, city, state, occupation, bank_balance: float, credit_score: int, credit_history):
        super().__init__(f_name, l_name, age, city, state)
        self.occupation = occupation 
        self.bank_balance = bank_balance 
        self.credit_score = credit_score 
        self.credit_history = credit_history

class ProcessApplication(FinancialInfo):
    def __init__(self, f_name, l_name, age, city, state,
                 occupation, bank_balance, credit_score, credit_history):

        super().__init__(f_name, l_name, age, city, state,
                         occupation, bank_balance, credit_score, credit_history)
    def validate_age(self):
        if self.age < 18:
            raise ValueError("You are less than 18 years of age.")
        else:
            return True
    
    def validate_bank_balance(self):
        if self.bank_balance > 20000:
            return True 
        else:
            raise ValueError("You have less bank balance.")

    def validate_credit_score(self):
        if self.credit_score > 650 and self.credit_history in ["good", "excellent"]:
            return True 
        else:
            raise ValueError("You have either less credit score or below average credit history")

class GenerateCreditCard(ProcessApplication):
    def __init__(self, bank_balance, credit_score):
        super().__init__(None, None, None, None, None, None, bank_balance, credit_score, None)

    def generatecard(self):

        card_number = str(rd.randint(1000, 9999)) + str(rd.randint(1000, 9999)) + str(rd.randint(1000, 9999))  # 123456789101 
        credit_limit = None
        cvv = str(rd.randint(0, 9)) + str(rd.randint(0, 9)) + str(rd.randint(0, 9))

        if self.bank_balance in range(25000, 50000):
            credit_limit = 10000

        if self.credit_score in range(700, 750):
            credit_limit = credit_limit + 2000
        elif self.credit_score in range(751, 800):
            credit_limit = credit_limit + 5000 
        elif self.credit_score >= 801:
            credit_limit = credit_limit + 10000

        return card_number, credit_limit, int(cvv)
        
        
if __name__ == "__main__":

    applicant = ProcessApplication("irfan", "khan", 27, "chicago", "illinois", "developer", 25000.00, 700, "good")
    
    try: 
        applicant.validate_age()
        applicant.validate_bank_balance()
        applicant.validate_credit_score()
        print("Your Application is accepted.")

        card_generate = GenerateCreditCard(applicant.bank_balance, applicant.credit_score)
        card_number, credit_limit, cvv = card_generate.generatecard()

        print(f"Credit Card Number: {card_number}")
        print(f"Credit Card Limit: {credit_limit}")
        print(f"Card CVV: {cvv}") 
    
    except Exception as e:
        print(f"Application Rejected due to - {e}")

    
    
    