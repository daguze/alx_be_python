from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
display_current_datetime()
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date:"))
    dnow = datetime.now()
    delta = timedelta(days=number_of_days)
    future_date = dnow + delta
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
calculate_future_date()
