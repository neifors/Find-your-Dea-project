from math import sqrt
import utm
import geocoder


# g = geocoder.ip("me")
# print(g.json)
# print(g.latlng)

#?javascript
# window.navigator.geolocation.getCurrentPosition((position) => {
#     console.log(position.coords)
# })

        
class Dea():
    
    def __init__(self, x, y, id_code, address):
        self.x = float(x)
        self.y = float(y)
        self.id = id_code
        self.address = address
        
    @property
    def longitude(self):
        return utm.to_latlon(self.x, self.y, 30, "N")[0]
    
    @property
    def latitude(self):
        return utm.to_latlon(self.x, self.y, 30, "N")[1]
    
    def get_distance(self,x_user,y_user):
        leg1 = abs(x_user - self.x)
        leg2 = abs(y_user - self.y)
        distance = sqrt(leg1**2 + leg2**2)
        return distance
        
    def get_real_distance(self,user_coordinates):
        dea_pos = (self.latitude,self.longitude)
        return distance.distance(user_coordinates,dea_pos ).m



def create_dea(deafile):
    address = deafile.direccion_ubicacion+' '+deafile.direccion_portal_numero
    obj =  Dea(deafile.x_utm,deafile.y_utm,deafile.codigo_dea, address)
    return obj


def dea_by_distance(datafile, user_lat, user_long):
    # devuelve el dea mas cercano
    distance = 1000000000
    print(user_lat, user_long)
    coordinates = utm.from_latlon(float(user_lat),float(user_long))
    for dea in datafile:
        aux_dea = create_dea(dea)
        aux_distance = aux_dea.get_distance(coordinates[0], coordinates[1])
        if aux_distance < distance: 
            dea_latlong = (aux_dea.latitude, aux_dea.longitude)
            distance = aux_distance
            result = dea
    return result, dea_latlong, distance