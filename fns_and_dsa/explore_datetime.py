from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date




def calculate_future_date(current_date):
    add_time = input("Enter the number of days to add to the current date: ")
    the_add_time = int(add_time)
    future_date = current_date + timedelta(days=the_add_time)
    print("future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))
    return future_date

if __name__ == "__main__":
    current = display_current_datetime()
    calculate_future_date(current)

