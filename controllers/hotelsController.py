from flask_restful import Resource, reqparse
from models.hotelModel import HotelModel

hotelsList = [{
    'hotel_id': 1,
    'name': 'AlphaHotel',
    "star": 4.5,
    'dayPrice': 1000.00,
    "city": "Juiz de Fora"
}, {
    'hotel_id': 2,
    'name': 'BettaHotel',
    "star": 4.3,
    'dayPrice': 130.00,
    "city": "Rio de janeiro"
}, {
    'hotel_id': 3,
    'name': 'GameHotel',
    "star": 4.1,
    'dayPrice': 12000.00,
    "city": "São Paulo"
}
]


    
class Hotels(Resource):
    def get(self):
        return {"hotels": hotelsList}
    
class Hotel(Resource):
    
    arg = reqparse.RequestParser()
    arg.add_argument("name")
    arg.add_argument('stars')
    arg.add_argument('dayPrice')
    arg.add_argument('city')
        

    def find_all(hotel_id): 
        for hotel in hotelsList:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    
    def get(self, hotel_id):
        hotel = Hotel.find_all(hotel_id)
        if(hotel):
            return hotel
        return {"message": "hotel not found"}
    
    def post(self, hotel_id):

        data = Hotel.arg.parse_args()
        hotel_object = HotelModel(hotel_id, **data)
        new_hotel = hotel_object.json()
        # new_hotel = { "hotel_id": hotel_id, **data }
        hotelsList.append(new_hotel)
        return new_hotel, 200
        
    
    def put(self, hotel_id):
        data = Hotel.arg.parse_args()
        hotel_object = HotelModel(hotel_id, **data)
        new_hotel = hotel_object.json()
        hotel = Hotel.find_all(hotel_id)
        if hotel:
            hotel.update(new_hotel)
            return new_hotel, 200
        hotelsList.append(new_hotel)
        return new_hotel, 201
    
    def delete(self, hotel_id):
        global hotelsList
        hotelsList = [hotel for hotel in hotelsList if hotel['hotel_id'] != hotel_id] # hotel para cada hotel dentro de hoteis (Like map?)
        return {'message': "hotel deleted"}