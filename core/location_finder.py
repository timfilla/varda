import geocoder

class LocationFinder:
    def __init__(self):
        self.lat = None
        self.lon = None

        while True:
            method = input(
                'Choose method for determining location: (1) System location or (2) Enter a latitude and longitude. -> ')
            if method == '1':
                locator = SystemLocation
                break
            elif method == '2':
                locator = LatLon
                break
            else:
                print('Invalid input. Please enter one of the numbers listed.')

        coords = locator.get_latlon()
        self.set_lat(coords['lat'])
        self.set_lon(coords['lon'])

    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    def set_lat(self, lat):
        self.lat = lat

    def set_lon(self, lon):
        self.lon = lon

class SystemLocation:
    def __init__(self):
        pass

    @staticmethod
    def get_latlon():
        g = geocoder.ip('me')
        return {'lat': g.current_result.lat, 'lon': g.current_result.lng}

class LatLon:
    def __init__(self):
        pass

    @staticmethod
    def get_latlon(self):
        while True:
            try:
                lat = float(input('Enter a latitude: '))
            except ValueError:
                print('Invalid input. Enter a decimal number.')
            else:
                break
        while True:
            try:
                lon = float(input('Enter a longitude: '))
            except ValueError:
                print('Invalid input. Enter a decimal number.')
            else:
                return {'lat': lat, 'lon': lon}
