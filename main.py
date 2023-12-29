from tkinter import *
root = Tk()
entry = Entry()

d_label = Label(text='Enter the amount you want to deposit or withdraw below /n and click the appropriate button.',font=('verdana',14,'bold'))
d_label.grid(row=1,column=1,columnspan=5)

class BankSystemGUI():
    def __init__(self):
        self.balance = 1000
        self.user_input = Entry(font=('verdana',10,'bold'))
        self.user_input.grid(row=2,column=1,columnspan=5)


    def deposit(self):
      d_input = float(self.user_input.get())            
      self.balance += d_input
      d_label.config(text='Deposit Successful. Your new balance is {}'.format(self.balance))

    


    def withdraw(self):
         d_input = eval(Entry.get(self.user_input))
         if d_input > self.balance:
                 d.label.configure(text='Insufficient Balance n would you like an overdraft? yes/no \n ') 
                 d_input2 = Entry.get(self.user_input)
                           if d_input2 == 'yes':
                                        
               d_label.configure(text='Your request is being reviewed.')
             else:
                 d.label.configure(text='Please try again later')
         else:
             self.balance-=d_input
             d.label.configure(text='Withdrawal Successful. Your new balance is {}'.format(self.balance))

bank = BankSystemGUI()

deposit_button = Button(text='Deposit',font=('verdana',18,'italic'),bg='green',command=bank.deposit, fg='black')

withdraw_button = Button(text='Withdraw',font=('verdana',18,'italic'),bg='blue',command=bank.withdraw, fg='black')

                         
deposit_button.grid(row=4,column=1)
withdraw_button.grid(row=4,column=4)

mainloop()

                                                    
                