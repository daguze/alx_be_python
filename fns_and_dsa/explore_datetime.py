import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
display_current_datetime()
def calculate_future_date():
    number_of_days = int(input("Enter number of days to add: "))
    dnow = datetime.datetime.now()
    delta = datetime.timedelta(days=number_of_days)
    future_date = dnow + delta
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
calculate_future_date()
