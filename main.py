from booking.booking import Booking
import time

try:
    with Booking() as bot:
        bot.first_page(currency='PLN')
        bot.skip()
        bot.select_destination('Zakopane')
        # bot.currency()
        bot.select_dates(check_in="2024-07-10", check_out="2024-07-18")
        bot.select_occupancy(5)
        bot.search_click()
        bot.filters()
        bot.results()

        time.sleep(5)
except Exception as e:
    if "in PATH" in str(e):
        print("Add webdriver to PATH")
    else:
        print("kek")
        raise

    print("exiting...")
