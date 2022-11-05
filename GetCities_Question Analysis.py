# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:56:14 2022

@author: wilso
"""

import pandas as pd
import os

os.chdir('PATHWAY')

Survey = pd.read_excel('Scrubbed Survey Simple Variables.xlsx', 
                       sheet_name = "Survey")

# SQ3 = Gender Identity
# SQ4 = Race
# SQ9 = Emp Type
# SQ10 = Caregiver
# SQ16 = Plan to stay
# SQ24 = Tenure
# SQ25 = Career Advancement
# SQ27 = Someone to give career advice
# SQ28 = Someone to help them get promoted
# SQ34 = Compensation Equity
# SQ35 = Compensation
# SQ36 = Promotion Passed-up
# SQ39 = Healthcare Related Benefits
# SQ40 = Remote
# SQ41 = Leave with no remote

Survey.SQ3.value_counts()
Survey.SQ4.value_counts()
Survey.SQ9.value_counts()
Survey.SQ10.value_counts()
Survey.SQ24.value_counts()

# Subset dataset to intermediate to senior tenure

def encoder(df, var, newvar):
    df[var] = df[var].astype('category')
    df[newvar] = df[var].cat.codes
    
    return df

Survey = encoder(Survey, 'SQ24', 'SQ24c')

Survey_HT = Survey[(Survey['SQ9'] == "Work full-time") & 
                   (Survey['SQ24c'] < 7) & (Survey['SQ24c'] > 3)]


Survey_HT.SQ25.value_counts()
Survey_HT.SQ25.value_counts(normalize = True)

Survey.SQ35.value_counts(normalize = True)

# Subset dataset to intermediate to senior tenure by race

Survey_HT_B = Survey[(Survey['SQ9'] == "Work full-time") & 
                   (Survey['SQ24c'] < 7) & (Survey['SQ24c'] > 3) &
                   (Survey['SQ4'] == 'Black or African American')]

Survey_HT_B.SQ25.value_counts()
Survey_HT_B.SQ25.value_counts(normalize = True)

Survey_HT_B.SQ35.value_counts()
Survey_HT_B.SQ35.value_counts(normalize = True)


Survey_HT_L = Survey[(Survey['SQ9'] == "Work full-time") & 
                   (Survey['SQ24c'] < 7) & (Survey['SQ24c'] > 3) &
                   (Survey['SQ4'] == 'Hispanic or Latino')]

Survey_HT_L.SQ25.value_counts()
Survey_HT_L.SQ25.value_counts(normalize = True)

Survey_HT_L.SQ35.value_counts()
Survey_HT_L.SQ35.value_counts(normalize = True)

# Subset dataset to full time workers & parents/caregivers

Survey = encoder(Survey, 'SQ10', 'SQ10c')

Survey_CT = Survey[(Survey['SQ9'] == "Work full-time") & 
                     (Survey['SQ10c'] == 5) |
                     (Survey['SQ10c'] == 2) |
                     (Survey['SQ10c'] == 6) |
                     (Survey['SQ10c'] == 3) |
                     (Survey['SQ10c'] == 0)]

Survey_CT.SQ36.value_counts()
Survey_CT.SQ36.value_counts(normalize = True)

# Subset to full time

Survey_FT = Survey[(Survey['SQ9'] == "Work full-time")]

FirstBenefit = Survey_FT['SQ39'].str.split(',', n = 1, expand = False).str[0]
FirstBenefit.value_counts()
FirstBenefit.value_counts(normalize = True)

# Subset to Full time hybrid/remote workers

Survey_RFT = Survey[(Survey['SQ9'] == "Work full-time") &
                    (Survey['SQ40'] != "We all work in-person")]

Survey_RFT.SQ41.value_counts()

# Black and Latina Women
Survey_BLW = Survey[((Survey['SQ3'] == "Woman") |
                    (Survey['SQ3'] == "Genderqueer/ Nonbinary, Woman") |
                    (Survey['SQ3'] == "Woman, Genderqueer/ Nonbinary") |
                    (Survey['SQ3'] == "Transgender, Woman") |
                    (Survey['SQ3'] == "Woman, Transgender")) &
                    ((Survey['SQ4'] == 'Black or African American') |
                    (Survey['SQ4'] == 'Hispanic or Latino'))]

Survey_BLW.SQ34.value_counts()
Survey_BLW.SQ34.value_counts(normalize = True)

# White Women
Survey_WW = Survey[((Survey['SQ3'] == "Woman") |
                    (Survey['SQ3'] == "Genderqueer/ Nonbinary, Woman") |
                    (Survey['SQ3'] == "Woman, Genderqueer/ Nonbinary") |
                    (Survey['SQ3'] == "Transgender, Woman") |
                    (Survey['SQ3'] == "Woman, Transgender") &
                    (Survey['SQ4'] == 'Black or African American')) &
                    ((Survey['SQ4'] == 'White or Caucasian') |
                    (Survey['SQ4'] == 'White, but I am an immigrant'))]

Survey_WW.SQ34.value_counts()
Survey_WW.SQ34.value_counts(normalize = True)

# Stay in field by race

Survey_Stay = Survey[Survey['SQ16'] != 
                     'I plan to exit technology in 12 months or less']

Survey_Stay.SQ27.value_counts()
Survey_Stay.SQ27.value_counts(normalize = True)

Survey_Stay.SQ28.value_counts()
Survey_Stay.SQ28.value_counts(normalize = True)


Survey_BStay = Survey[(Survey['SQ16'] != 
                     'I plan to exit technology in 12 months or less') &
                     (Survey['SQ4'] == 'Black or African American')]

Survey_BStay.SQ27.value_counts()
Survey_BStay.SQ27.value_counts(normalize = True)

Survey_BStay.SQ28.value_counts()
Survey_BStay.SQ28.value_counts(normalize = True)

Survey_LStay = Survey[(Survey['SQ16'] != 
                     'I plan to exit technology in 12 months or less') &
                     (Survey['SQ4'] == 'Hispanic or Latino')]

Survey_LStay.SQ27.value_counts()
Survey_LStay.SQ27.value_counts(normalize = True)

Survey_LStay.SQ28.value_counts()
Survey_LStay.SQ28.value_counts(normalize = True)