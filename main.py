# ------------------------------------------------FORMAT IMPORTED CLASSES----------------------------------------------#
import time

from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.google_sheet_data()

# --------------------------------------------------------------------------------------------------------------------#
from flight_data import FlightData
flight_data = FlightData

# --------------------------------------------------------------------------------------------------------------------#
from flight_search import FlightSearch  # USE LATER IN THE CODE

# --------------------------------------------------------------------------------------------------------------------#
from notification_manager import NotificationManager
notification_manager = NotificationManager

# --------------TESTING PURPOSE------------------------#
# my_city = "LON"
# -------------------------------------------------------MAIN CODES ---------------------------------------------------#
flight_search = FlightSearch()
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.add_iata_code()

for destination in sheet_data:
    try:
        flights = flight_search.flight_info(destination['iataCode'])
        while True:
            # ------ 30 minutes time delay---#
            time.sleep(1800)
            if int(flights.price) < destination['lowestPrice']:

                message = (f"Flight from {flights.my_city} to {flights.destination_city} is scheduled on "
                           f"{flights.departure_date} "
                           f"from {flights.departure_airport} airport for price £{flights.price}."
                           f"Click on the link to book the flight {flights.flight_link}")

                if flights.stop_overs > 0:
                    message += f"\nFlight has {flights.stop_overs} stop over, via {flights.via_city}."
                print(message)
                notification_manager(message)
            else:
                print("Still checking the price")
    except (IndexError, AttributeError):
        pass
        # print(f"No price found for {destination['city']}")

# -------------------------------------------------Google_code example ----------------------------------------------#
# https://www.google.co.uk/flights?hl=en#flt=STN.SXF.2020-08-25*SXF.STN.2020-09-08
# https://www.google.co.uk/flights?hl=en#flt=LON.GIB.2021-11-19*GIB.LON.2021-12-17
# -------------------------------------------------Google_code-----------------------------------------------------#
# "https://www.google.co.uk/flights?hl=en#flt={my_city}.{flights.destination_airport}."
# "{flights.departure_date}*{flights.destination_airport}.{my_city}.{flights.return_date}"
