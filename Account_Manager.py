import tkinter as tk
import ttkbootstrap as ttk

def isAccountUnique(User:dict, name): # Check if any existing accounts the user have has the same name as the new account
    for accName in User.UserInfo["Accounts"]:
        if accName == name:
           return False
    return True

def newAccount(Information: dict): # create a new account
    newInfo = {}
    newInfo["Amount"] = Information["Amount"] or 0,
    newInfo["Frozen"] = Information["Frozen"] or False # If account is frozen then do not make any transactions
    newInfo["Account_Type"] = Information["Account_Type"] or "N/A" # There must be a valid account type (credit or debit)
    return newInfo
        

class Create_User():
    def __init__(self,Information: dict):
        # set information in a table
        self.UserInfo = {
            "Personal_Information": {
                "Name":Information["personal"]["Name"] or "N/A", # First_Middle_Last
                "Email":Information["personal"]["Email"] or "N/A",
                "Ethnicity":Information["personal"]["Ethnicity"] or "N/a",
                "Birthdate":Information["personal"]["Birthdate"] or "N/A",
                "Phone_Number":Information["personal"]["Phone_Number"] or "N/A",
                "Id":0, # this will be altered later
            },
            "Accounts":{},
            "Settings":{"All_Acc_Frozen":False}
        }

        # create default deposit account
        self.UserInfo["Accounts"]["Checkings"] = newAccount(Information["DefaultAccount"])

        print(self.UserInfo["Accounts"]["Checkings"]["Amount"])
        print("User Created! ", self.UserInfo)

newAcc = Create_User({"personal": # example
                      {"Name":"John","Email":"John.doe@gmail.com","Ethnicity":"White","Birthdate":"1/1/1000","Phone_Number":"1234567890"},
                      "DefaultAccount":
                      {"Amount":25,"Frozen":False,"Account_Type":"Debit"}
                      })
