def time_string(hours,minutes,time_format):
    if time_format == '24':
        # Format for 24-hour time
        return f"{hours}:{minutes}"
    else:
        # Format for 12-hour time
        period = 'AM' if hours < 12 else 'PM'
        hour_12 = hours % 12
        hour_12 = 12 if hour_12 == 0 else hour_12  # Handle midnight and noon
        return f"{hour_12}:{minutes:02} {period}"

print(f"The time is {time_string(11,15,'24')} ")
