from booking.booking import Booking
import time

with Booking() as bot:
    bot.first_page(currency='PLN')
    bot.skip()
    bot.select_destination('Zakopane')
    # bot.currency()

    time.sleep(5)



    print("exiting...")