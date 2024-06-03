from booking.booking import Booking
import time

with Booking() as bot:
    bot.first_page(currency='PLN')
    bot.skip()
    bot.select_destination('Zakopane')
    # bot.currency()
    time.sleep(3)
    bot.select_dates(check_in="2024-06-16", check_out="2024-06-18")
    bot.select_occupancy(1)

    time.sleep(5)



    print("exiting...")