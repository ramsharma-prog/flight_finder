import requests
from pprint import pprint
import datetime as dt
from datetime import timedelta
from flight_data import FlightData

# ------------------------------------------------FORMAT IMPORTED CLASSES----------------------------------------------#
flight_data = FlightData
# -------------------------------------------KIWI API'S DATA (DO NOT TOUCH THIS CODE)----------------------------------#

KIWI_END_POINT = "https://tequila-api.kiwi.com"
KIWI_API_KEY = "fkK77y1VRpXRRzI6AOFXasnsWEpNaw4w"

header = {"apikey": KIWI_API_KEY}
my_city = "JFK"

# ----------------------------------------------------TIME SET UP------------------------------------------------------#
current_time = dt.datetime.now()
date = current_time.date() + timedelta(7)
tomorrow_date = date.strftime("%d/%m/%Y")

six_months = date + timedelta(180)
six_months_date = six_months.strftime("%d/%m/%Y")


# -----------------------------------------------------CODES------------------------------------------------------------#
# This class is responsible for talking to the Flight Search API.
class FlightSearch():

    def destination_code(self, city_name):

        query = {"term": city_name, "location_types": "city"}

        kiwi_response = requests.get(url=f"{KIWI_END_POINT}/locations/query", headers=header, params=query)
        iata_code = kiwi_response.json()['locations'][0]['code']
        # -----------TESTING PURPOSE (To review iata codes)------------------------#
        print(iata_code)
        return iata_code

    def flight_info(self, destination):
        flight_parameters = {
            "fly_from": my_city,
            "fly_to": destination,
            "date_from": tomorrow_date,
            "date_to": six_months_date,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        flight_search_response = requests.get(url=f"{KIWI_END_POINT}/v2/search", params=flight_parameters,
                                              headers=header)

        try:
            flight_response_data = flight_search_response.json()["data"][0]
            # -----------TESTING PURPOSE (To review all the data from flight)------------------------#
            pprint(f'Direct flight whole data: {flight_response_data}')
            # print("\n")
        except IndexError:
            pass

        except:
            flight_parameters["max_stopovers"] = 1
            flight_search_response = requests.get(url=f"{KIWI_END_POINT}/v2/search", params=flight_parameters,
                                                  headers=header)
            flight_response_data = flight_search_response.json()["data"][0]
            # -----------TESTING PURPOSE (To review all the data from flight)------------------------#
            # pprint(f"Stop over flight  whole data:  {flight_response_data}")
            # print("\n")

            flight_data = FlightData(
                price=flight_response_data['price'],
                departure_airport= flight_response_data ['route'] [0] ['flyFrom'],
                departure_city= flight_response_data ['route'] [0] ['cityFrom'],
                departure_date= flight_response_data['route'][0]['local_departure'].split('T')[0],
                destination_airport= flight_response_data ['route'] [1] ['flyTo'],
                return_date= flight_response_data['route'][2]['local_departure'].split('T')[0],
                destination_city= flight_response_data ['route'][1]['cityTo'],
                flight_link= flight_response_data['deep_link'],
                stop_overs= 1,
                via_city= flight_response_data ['route'] [0] ['cityTo'],
            )
            # -----------TESTING PURPOSE (To review all the data from flight)------------------------#
            pprint(f"Stop over flight tp {flight_data.destination_city} via {flight_data.via_city} £{flight_data.price}")
            return flight_data

        else:
            flight_data = FlightData(
                price=flight_response_data['price'],
                departure_airport=flight_response_data['flyFrom'],
                departure_city=flight_response_data['cityFrom'],
                departure_date=flight_response_data['route'][0]['local_departure'].split('T')[0],
                destination_airport=flight_response_data['flyTo'],
                return_date=flight_response_data['route'][1]['local_departure'].split('T')[0],
                destination_city=flight_response_data['cityTo'],
                flight_link=flight_response_data['deep_link'],


            )
            # -----------TESTING PURPOSE (To review all the data from flight)------------------------#
            pprint(f" Direct flight to {flight_data.destination_city} for £{flight_data.price}")

            return flight_data

flight = FlightSearch()

flight.flight_info("DPS")