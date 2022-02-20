# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 18:57:09 2022

@author: amitt
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Loan_Eligibilty(BaseModel):
      Gender:int 
      Married: int
      TotalIncome_log:float
    