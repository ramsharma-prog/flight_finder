# This class is responsible for structuring the flight data.
class FlightData():
    def __init__(self,price,departure_city,departure_airport,destination_city,destination_airport,departure_date,
                 return_date,flight_link,stop_overs = 0,via_city = ""):
        self.price = price
        self.my_city = departure_city
        self.departure_airport = departure_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date
        self.flight_link = flight_link
        self.stop_overs = stop_overs
        self.via_city = via_city






