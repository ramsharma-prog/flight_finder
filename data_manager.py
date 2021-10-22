import requests

# -------------------------------------GOOGLE SHEET END POINT (DO NOT TOUCH THIS CODE)---------------------------------#
SHEETY_PRICE_END_POINT = "........................................."

# ------------------add_destination_dat() ADMIN--TESTING PURPOSE (UPDATE FLIGHT DATA)----------------------------------#
CITY = "LA"
IATA_CODE = "TESTING"
PRICE = "110"


# ----------------------------------------------------DATA MANAGER CODE------------------------------------------------#

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        # ----------TESTING PURPOSE--------#
        # self.google_sheet_data()
        # self.add_iata_code()

        # print(self.destination_data)
        # self.add_destination_name()

    def google_sheet_data(self):
        fly_to = requests.get(url=SHEETY_PRICE_END_POINT)
        sheet_response = fly_to.json()
        self.destination_data = sheet_response['prices']
        return self.destination_data

    def add_iata_code(self):
        for city in self.destination_data:
            iata_data = {
                "price":
                    {"iataCode": city["iataCode"],
                     }
            }
            response = requests.put(url=f"{SHEETY_PRICE_END_POINT}/{city['id']}", json=iata_data)
            print(response)

    # -------------------------------------------------ADDITIONAL CODE(NOT IN USE)-------------------------------------#

    def add_destination_name(self):
        iata_data = {
            "price":
                {"city": CITY,
                 "iataCode": IATA_CODE,
                 "lowestPrice": PRICE,

                 }
        }

        requests.post(f"{SHEETY_PRICE_END_POINT}", json=iata_data)


# ----------------------------------------------CALLING CLASS ( TESTING)----------------------------------------------#
# data = DataManager()
# --------------------------------------------------END----------------------------------------------------------------#
