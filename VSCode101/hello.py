import datetime

def say_hello(name):
    print("Hello, " + name)

say_hello("VS Code")

def say_day_of_week(d):
    print("Today is " + d.strftime("%A"))

say_day_of_week(datetime.date.today())
