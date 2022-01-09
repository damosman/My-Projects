print("""________________________________________________________________________________________________________________________________
  _      _                                                         _____                 __                                     
  |  |  /          /                                               /    )                / |    ,         /   ,                 
--|-/|-/-----__---/----__----__---_--_----__------_/_----__-------/----/----__---_--_---/__|-------)__---/--------__----__---__-
  |/ |/    /___) /   /   ' /   ) / /  ) /___)     /    /   )     /    /   /   ) / /  ) /   |  /   /   ) /   /   /   ) /___) (_ `
__/__|____(___ _/___(___ _(___/_/_/__/_(___ _____(_ __(___/_____/____/___(___(_/_/__/_/____|_/___/_____/___/___/___/_(___ _(__)_""" '\n')

try:
    from datetime import datetime
    from datetime import time
    import string
    import random

    # booking_day, month and time for flight passenger.
    booking_day = int(input("Enter the day: "))
    booking_month= int(input("Enter the month: "))
    booking_time = int(input("Enter a time in the format Hours: "))
    booking_year = 2022

    #booking code
    # code = []
    # for i in range(10):
    #     num = random.randint(0,10)
    #     alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    #     num_alphabet = code.append(num)

    booking_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 10))

    # datetime object containing current date and time
    now = datetime.now()

    # datetime as dt (alias) because datetime from datetime returns error.
    import datetime as dt
    booking_date = dt.datetime(booking_year, booking_month, booking_day, booking_time)
    checkin_start_time = 2
    checkIn_hours = dt.datetime(booking_year, booking_month, booking_day, checkin_start_time)
    if booking_date > now:
        checkIn_time = booking_time - checkin_start_time
        if checkIn_time <= checkin_start_time:
            checkIn_time += 24
        checkIn_time = str(checkIn_time) + ':' + '00' + ':' + '00.'
        print("\n" "Thank You for booking with DamAirlines, Your booking date is", booking_date, "and your booking number is", booking_code,"."  '\n' "Your check-in time is from", checkIn_time,
              "Kindly check your email for booking confirmation.")
    else:
        print("Error! Past date cannot be entered")

except( TypeError, ValueError, NameError):
    print("Please Enter a valid date")


