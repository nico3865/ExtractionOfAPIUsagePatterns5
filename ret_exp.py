


# RRSP scenario: '30 years of frugal software engineer':
number_of_years_contributing_yearly = 30
RRSP_contrib_yearly = 18000
saved_in_taxes = 10147 # thats for an imagined income of 100,000 :P
stock_yearly_compounding = 1.10
previous_balance = 0
for x in range(0, number_of_years_contributing_yearly):
    new_balance = (previous_balance + (RRSP_contrib_yearly + saved_in_taxes) ) * stock_yearly_compounding
    # print(new_balance)
    previous_balance = new_balance
print("RRSP scenario: '30 years of frugal software engineer' --> "+str(previous_balance))
# 6,359,618.55 @ like 200,000$/year income
# and now you will pay
#   - 30% tax on anything you withdraw after 71
#   - 40-60% tax on anything you withdraw before 71



# NON_REGIST scenario: '30 years of frugal software engineer':
number_of_years_contributing_yearly = 30
NON_REGIST_contrib_yearly = 18000
# Your deduction limit is 18% of your earned income, to a maximum value for the year. The maximum RRSP contribution for tax year 2016 is $26,930.
# As most people filed their tax return before the income tax deadline, it’s now a matter of waiting for that juicy tax return.  Most consider tax refunds to be “free money” that was unaccounted for.  And it’s true, you can do whatever you want with the money.  However, in my opinion, tax returns should be used wisely as it’s basically money that you overpaid to the government during the year.
#   - The conclusion was that RRSP’s are superior only if the tax refund is reinvested or used to pay down debt.
saved_in_taxes = 0
stock_yearly_compounding = 1.10
previous_balance = 0
for x in range(0, number_of_years_contributing_yearly):
    new_balance = (previous_balance + (NON_REGIST_contrib_yearly + saved_in_taxes) ) * stock_yearly_compounding
    # print(new_balance)
    previous_balance = new_balance
print("NON_REGIST scenario: '30 years of frugal software engineer' --> "+str(previous_balance))
# 4,523,585.62 @ like 200,000$/year income
# and now you will pay
#   - max approx 15% of income tax on this (30% of 50% of what you take out)



# TFSA scenario: 'anyone has 5500 per year':
number_of_years_contributing_yearly = 30
TFSA_contrib_yearly = 5500
saved_in_taxes = 0
stock_yearly_compounding = 1.10
previous_balance = 0
for x in range(0, number_of_years_contributing_yearly):
    new_balance = (previous_balance + (TFSA_contrib_yearly + saved_in_taxes) ) * stock_yearly_compounding
    # print(new_balance)
    previous_balance = new_balance
print("TFSA scenario: 'anyone has 5500 per year' --> "+str(previous_balance))
# 995,188.83

# TFSA scenario: 'anyone has 5500 per year - but starting with an allowed TFSA of 63,000':
number_of_years_contributing_yearly = 30
TFSA_contrib_yearly = 5500
saved_in_taxes = 0
stock_yearly_compounding = 1.10
initial_balance = 63000
previous_balance = initial_balance
for x in range(0, number_of_years_contributing_yearly):
    new_balance = (previous_balance + (TFSA_contrib_yearly + saved_in_taxes) ) * stock_yearly_compounding
    # print(new_balance)
    previous_balance = new_balance
print("TFSA scenario: 'anyone has 5500 per year - but starting with an allowed TFSA of 63,000' --> "+str(previous_balance))
# 2,094,501.1802074756


# RRSP scenario: '30 years of frugal software engineer' --> 5,093,014.58
# NON_REGIST scenario: '30 years of frugal software engineer' --> 3,256,981.64
# TFSA scenario: 'anyone has 5500 per year' --> 995,188.83


# RRSP scenario: '30 years of frugal software engineer' --> 5,093,014.58
# NON_REGIST scenario: '30 years of frugal software engineer' --> 3,256,981.64
# TFSA scenario: 'anyone has 5500 per year' --> 995188.8372676293
# TFSA scenario: 'anyone has 5500 per year - but starting with an allowed TFSA of 63,000' --> 2,094,501.18


