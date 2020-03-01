from datetime import date

def dayInfo():
    now = date.today()
    d2 = now.strftime("%B %d, %Y")
    print("It is " + d2)

def activationPhrases():
    act = []

    act.append("whats the date")
    act.append("what day is it today")
    act.append("tell me about today")

    return act
