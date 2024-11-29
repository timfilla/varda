from astropy.coordinates import SkyCoord, AltAz, EarthLocation, Galactic
from astropy.time import Time
import astropy.units as u

class AstroCalculator:
    def __init__(self, lat, lon, obs_time, data):
        self.lat = lat
        self.lon = lon
        self.obs_time = obs_time
        self.data = data
        self.observer_location = EarthLocation(lat=self.lat, lon=self.lon)

    @staticmethod
    def hours_to_dec(ra_string):
        h = float(ra_string[:2])
        m = float(ra_string[3:5])
        s = float(ra_string[6:10])
        return h + m / 60 + s / 3600

    @staticmethod
    def deg_to_dec(dec_string):
        d = float(dec_string[1:3])
        m = float(dec_string[4:6])
        s = float(dec_string[7:11])
        deci = d + m / 60 + s / 3600
        if dec_string[0] == '-':
            deci = -deci
        return deci

    def calc_altaz(self, target):
        # Get RA and DEC and convert to SkyCoord compatible format
        ra_data = self.data.loc[self.data['name'] == target, 'ra'].iloc[0]
        dec_data = self.data.loc[self.data['name'] == target, 'dec'].iloc[0]
        ra_hours = self.hours_to_dec(ra_data)
        dec_hours = self.deg_to_dec(dec_data)

        # Specify the RA/Dec coordinates to convert
        ra = ra_hours * u.hourangle
        dec = dec_hours * u.deg

        # Create a SkyCoord object for the RA/Dec coordinates
        sc_obj = SkyCoord(ra=ra, dec=dec, frame='icrs')

        # Convert RA/Dec to Alt/Az and return
        return sc_obj.transform_to(AltAz(obstime=self.obs_time, location=self.observer_location))

class ObjectFinder(AstroCalculator):
    def __init__(self, target, lat, lon, obs_time, data):
        super().__init__(lat, lon, obs_time, data)
        self.target = target
        altaz = super().calc_altaz(self.target)
        print(f'Object {target} is currently located at Azimuth {altaz.az} and Altitude {altaz.alt}.')
