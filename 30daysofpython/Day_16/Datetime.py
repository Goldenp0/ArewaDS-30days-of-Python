from datetime import datetime, timedelta

# Get current date, month, year, hour, minute, and timestamp
current_date = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year
current_hour = datetime.now().hour
current_minute = datetime.now().minute
current_timestamp = datetime.timestamp(datetime.now())

print("Current Date:", current_date)
print("Current Month:", current_month)
print("Current Year:", current_year)
print("Current Hour:", current_hour)
print("Current Minute:", current_minute)
print("Current Timestamp:", current_timestamp)
print()

# Format the current date
formatted_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted Date:", formatted_date)
print()

# Convert time string to time
time_string = "5 December, 2019"
converted_time = datetime.strptime(time_string, "%d %B, %Y")
print("Converted Time:", converted_time)
print()

# Calculate time difference between now and new year
new_year = datetime(current_year + 1, 1, 1)
time_difference_to_new_year = new_year - datetime.now()
print("Time difference to New Year:", time_difference_to_new_year)
print()

# Calculate time difference between 1 January 1970 and now (UNIX epoch time)
epoch_time = datetime(1970, 1, 1)
time_difference_to_epoch = datetime.now() - epoch_time
print("Time difference to UNIX Epoch:", time_difference_to_epoch)
