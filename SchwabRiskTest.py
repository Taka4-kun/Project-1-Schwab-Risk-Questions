from ast import Return
from re import A


category = ''

time_horizon_score = 0
risk_tolorence_score = 0

answer_one = input("""Question 1: When do you plan to withdraw money from your investments?
A) Less than 3 years
B) 3 to 5 years
C) 6 to 10 years
D) 11 years or more 

""")
if answer_one == 'A':
    time_horizon_score += 1
elif answer_one == 'B':
    time_horizon_score += 3
elif answer_one == 'C':
    time_horizon_score += 7
elif answer_one == 'D':
    time_horizon_score += 10
else:
    print('Sorry that is not a valid answer')

answer_two = input("""Question 2:Once you begin withdrawls from your investments, How fast do you plan to spend all of the funds?
A) Less than 2 years
B) 2 to 5 years
C) 6 to 10 years
D) 11 years or more 

""")
if answer_two == 'A':
    time_horizon_score += 0
elif answer_two == 'B':
    time_horizon_score += 1
elif answer_two == 'C':
    time_horizon_score += 4
elif answer_two == 'D':
    time_horizon_score += 8
else:
    print('Sorry that is not a valid answer')

answer_three = input("""Question 3:How would you describe your knowledge of investments as:
A) None
B) Limited
C) Good
D) Extensive 

""")
if answer_three == 'A':
    risk_tolorence_score += 1
elif answer_three == 'B':
    risk_tolorence_score += 3
elif answer_three == 'C':
    risk_tolorence_score += 7
elif answer_three == 'D':
    risk_tolorence_score += 10
else:
    print('Sorry that is not a valid answer')

answer_four = input("""Question 4: What amount of financial risk are you willing to take when you invest? 
A) Take lowe than average risks wxpecting to earn lower than average returns
B)Take average risks expecting to earn average returns
C) Take above average risks expecting to earn above average returns

""")
if answer_four == 'A':
    risk_tolorence_score += 0
elif answer_four == 'B':
    risk_tolorence_score += 4
elif answer_four == 'C':
    risk_tolorence_score += 8

else:
    print('Sorry that is not a valid answer')

answer_five = input("""Question 5: Please select the investments you currently own or have owned:
A) Bonds and /or bond funds
B) Stocks and/or stock funds
C) International securities and or international funds
    Example: You now own stock funds. In the past, you've purchased international securities, then your answer would be C

""")
if answer_five == 'A':
    risk_tolorence_score += 3
elif answer_five == 'B':
    risk_tolorence_score += 6
elif answer_five == 'C':
    risk_tolorence_score += 8
else:
    print('Sorry that is not a valid answer')

answer_six = input("""Question 6: Imagine that in the past three months, the overall stock market lost 25percent of it's value. An individual stock investment you  own also lost 25percent of it's value. What would you do?
A) Sell all of my shares
B) Sell some of my shares
C) Do noting
D) Buy more shares

""")
if answer_six == 'A':
    risk_tolorence_score += 0
elif answer_six == 'B':
    risk_tolorence_score += 2
elif answer_six == 'C':
    risk_tolorence_score += 5
elif answer_six == 'D':
    risk_tolorence_score += 8
else:
    print('Sorry that is not a valid answer')

answer_seven = input("""Question 7: Below you will see outlined the most likely best and worst case annual returns of five hypothetical investment plans. Which     range of outcome is most acceptable for you?

A) 
Average annual return: 2.6%
Best case: 10.8%
worst case: -5.1%

B) 
Average annual return: 4.1%
Best case: 19.2%
worst case: -10.6%

C) 
Average annual return: 5.6%
Best case: 27.6%
worst case: -16.4%

D) 
Average annual return: 6.1%
Best case: 36.0%
worst case: -21.7%

E) 
Average annual return: 7.2%
Best case: 42.5%
worst case: -25.8%
""")
if answer_seven == 'A':
    risk_tolorence_score += 0
elif answer_seven == 'B':
    risk_tolorence_score += 3
elif answer_seven == 'C':
    risk_tolorence_score += 6
elif answer_seven == 'D':
    risk_tolorence_score += 8
elif answer_seven == 'E':
    risk_tolorence_score += 10
else:
    print('Sorry that is not a valid answer')


def getRiskCategory(category):
    if time_horizon_score <= 4 and risk_tolorence_score <= 18:
        category = 'conservative'
        print("It seems that your risk level is conservative when it comes to investments!")
    # Moderately Conservative
    elif time_horizon_score <= 4 and risk_tolorence_score <= 31:
        category = 'moderately conservative'
        print("It seems that your risk level is moderately conservative when it comes to investments!")
    # Moderate
    elif time_horizon_score <= 4 and risk_tolorence_score <= 40:
        category = 'moderate'
        print("It seems that your risk level is moderate when it comes to investments!")
    elif time_horizon_score <= 5 and risk_tolorence_score <= 15:
        category = 'conservative'
        print("It seems that your risk level is conservative when it comes to investments!")
    elif time_horizon_score <= 5 and risk_tolorence_score <= 24:
        category = 'moderately conservative'
        print("It seems that your risk level is moderately conservative when it comes to investments!")
    elif time_horizon_score <= 5 and risk_tolorence_score <= 35:
        category = 'moderate'
        print("It seems that your risk level is moderate when it comes to investments!")
    elif time_horizon_score <= 5 and risk_tolorence_score <= 40:
        category = 'moderately aggresive'
        print("It seems that your risk level is moderately aggressive when it comes to investments!")
    elif time_horizon_score <= 9 and risk_tolorence_score <= 12:
        category = 'conservative'
        print("It seems that your risk level is conservative when it comes to investments!")
    elif time_horizon_score <= 9 and risk_tolorence_score <= 20:
        category = 'moderately conservative'
        print("It seems that your risk level is moderately conservative when it comes to investments!")
    elif time_horizon_score <= 9 and risk_tolorence_score <= 28:
        category = 'moderate'
        print("It seems that your risk level is moderate when it comes to investments!")
    elif time_horizon_score <= 9 and risk_tolorence_score <= 37:
        category = 'moderately aggresive'
        print("It seems that your risk level is moderately aggressive when it comes to investments!")
    elif time_horizon_score <= 9 and risk_tolorence_score <= 40:
        category = 'aggresive'
        print("It seems that your risk level is aggressive when it comes to investments!")
    #
    elif time_horizon_score <= 12 and risk_tolorence_score <= 11:
        category = 'conservative'
        print("It seems that your risk level is conservative when it comes to investments!")
    elif time_horizon_score <= 12 and risk_tolorence_score <= 18:
        category = 'moderately conservative'
        print("It seems that your risk level is moderately conservative when it comes to investments!")
    elif time_horizon_score <= 12 and risk_tolorence_score <= 26:
        category = 'moderate'
        print("It seems that your risk level is moderate when it comes to investments!")
    elif time_horizon_score <= 12 and risk_tolorence_score <= 34:
        category = 'moderately aggresive'
        print("It seems that your risk level is moderately aggressive when it comes to investments!")
    elif time_horizon_score <= 12 and risk_tolorence_score <= 40:
        category = 'aggresive'
        print("It seems that your risk level is aggressive when it comes to investments!")
    ##
    elif time_horizon_score <= 18 and risk_tolorence_score <= 10:
        category = 'conservative'
        print("It seems that your risk level is conservative when it comes to investments!")
    elif time_horizon_score <= 18 and risk_tolorence_score <= 17:
        category = 'moderately conservative'
        print("It seems that your risk level is moderately conservative when it comes to investments!")
    elif time_horizon_score <= 18 and risk_tolorence_score <= 24:
        category = 'moderate'
        print("It seems that your risk level is moderate when it comes to investments!")
    elif time_horizon_score <= 18 and risk_tolorence_score <= 31:
        category = 'moderately aggresive'
        print("It seems that your risk level is moderately aggressive when it comes to investments!")
    elif time_horizon_score <= 18 and risk_tolorence_score <= 40:
        category = 'aggresive'
        print("It seems that your risk level is aggressive when it comes to investments!")
    return (category)


category = getRiskCategory(category)
print(time_horizon_score)
print(risk_tolorence_score)
print(category)

if category == "conservative":
    print("""It looks like you are the type of investor who seeks current income and stability and are less concerned about growth. In this case the allocation that may inteerst you best is 
    Large-Cap Equity: 15%
    Small-Cap Equity: 0%
    International Equity: 5%
    Fixed Income: 50%
    Cash Investments: 30%
    
    Your average annual return should be around 7.4%""")
elif category == "moderately conservative":
    print("""It looks like you are the type of investor who seeks current income and stability, with a modest potental for increase in value. In this case the allocation that may inteerst you best is 
    Large-Cap Equity: 25%
    Small-Cap Equity: 5%
    International Equity: 10%
    Fixed Income: 50%
    Cash Investments: 10%""")
elif category == "moderate":
    print("""It looks like you are the type of investor who dose not need current income and want some growth potential. You are likely to entail some fluctuations in value, but presents less volatility than the overall equity market. In this case the allocation that may interest you best is 
    Large-Cap Equity: 35%
    Small-Cap Equity: 10%
    International Equity: 15%
    Fixed Income: 35%
    Cash Investments: 5%""")
elif category == "moderately aggresive":
    print("""It seems like you are a long-term investor who wants good enough growth potential and don't need current income. Entails a fair amount of volitility, but not as much as a portfolio invested exclusively in equities.vIn this case the allocation that may interest you best is 
    Large-Cap Equity: 45%
    Small-Cap Equity: 15%
    International Equity: 20%
    Fixed Income: 15%
    Cash Investments: 5% """)
elif category == "aggresive allocations":
    print("""You must be a long-term investor who wants high growth potential and don't need current income. May entail substantial year-to-year volitility in value in exchange for potentially high long-term returns. In this case the allocation that may interest you best is 
    Large-Cap Equity: 50%
    Small-Cap Equity: 20%
    International Equity: 25%
    Fixed Income: 0%
    Cash Investments: 5% """)

print("""


""")
print("Please remember this is just a test project. The information provided is based off of Charles Schwab's Investor profile questionnaire, and should not be used to decide on actual investments. This is just for educational purposes! ")
