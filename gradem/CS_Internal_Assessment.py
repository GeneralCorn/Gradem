# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] tags=[]
# # CS IA Preliminary Tests
# -

# **Key:**
# * C_ : comment
# * S_ : student
# * G_ : grade

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# + tags=[] jupyter={"source_hidden": true}
A, B, C, D = list(input("Enter A/B/C/D grades (no separation): "))
A, B, C, D = [int(x) for x in [A, B, C, D]]

S_Dict = {
    "Fname": input("Enter First Name:"),
    "Lname": input("Enter Last Name: "),
    "CriA": A,
    "CriB": B,
    "CriC": C,
    "CriD": D,
    "target_Grade": int(input("Target Grade: ")),
    "Gender": input("Gender: ")
}
Fname 


# + [markdown] tags=[]
# ### Grade Input 
#
# **S_Dict**: Dict for Fname, Lname, CriA-D grades
#
# **final_G()**: Returns final grade for student

# + jupyter={"source_hidden": true} tags=[]
def final_g():
    
    A = S_Dict["CriA"]
    B = S_Dict["CriB"]
    C = S_Dict["CriC"]
    D = S_Dict["CriD"]
    
    x = A+B+C+D
    
    if x < 5:
        return 1
    
    if x < 9:
        return 2
    
    if x < 14:
        return 3
    
    if x < 18:
        return 4
    
    if x < 23:
        return 5
    
    if x < 27:
        return 6
    
    if x <= 32:
        return 7
    
print("{0} {1}'s final Design grade is {2}".format(Fname, Lname, final_g()))
# -

# ### UNIT/Effort/ATL Skills

# **C_Modifiers**: Stores the effort level, ATL1/2 values. 
#
# *Parameters*: **E** (Effort), **A1G** (ATL1 Grade), **A2G** (ATL2 Grade), **U** (Unit), **A1** (ATL1), **A2** (ATL2)

# + jupyter={"source_hidden": true} tags=[]
E, A1G, A2G, U, A1, A2 = "E", "A1G", "A2G", "Unit", "A1", "A2"

def C_Modifiers(attr):
    
    i = input("Unit: ") #unit
    x = input("ATL1: ") #First atl
    y = input("ATL2: ") #Second atl
    
    # Effort Level + Restrictions  
    bool = True
    while bool:
        a = int(input("Effort Level (1-3): "))   
        if a not in [1,2,3]:
            print("Effort level is in range 1-3, please retry.")
            continue
        bool = False
        
    # ATL Grades + Restrictions 
    bool = True
    while bool:
        b = input("ATL1 Grade (EE,ME,AE,BE): ")
        c = input("ATL2 Grade (EE,ME,AE,BE): ")
        if (b not in ["EE","ME","AE","B"]) and (c not in ["EE","ME","AE","B"]):
            print("Please input the correct keywords. ")
            continue
        bool = False
                                     
    if attr == E:
        return a
    elif attr == A1G:
        return b
    elif attr == A2G:
        return c
    elif attr == U:
        return i
    elif attr == A1:
        return x
    elif attr == A2:
        return y
    else: 
        return "Value does not exist"
    
C_Modifiers(U)   


# -

# ### Comment Return

class C_Returner():
    
    S_GENDER = S_Dict["Gender"]
    
    def _init_(self, s): #initialize instances
        this.s = s


# ### Flask Deployment

# +
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
    # -







