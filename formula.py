exprestion=input("Enter your formula: ")
left_closing_bracket = exprestion.count("(")
right_closing_bracket = exprestion.count(")")
if left_closing_bracket == right_closing_bracket:
    print("The formula has same number of opening and closing paranthesis")
else:
    print("The formula has different number of opening and closing pranthesis\nFormula is invalid")
