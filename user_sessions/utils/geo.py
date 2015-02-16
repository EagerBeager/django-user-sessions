# -*- coding: utf-8 -*-
import warnings
from django.contrib.gis.geoip import HAS_GEOIP


_geoip = None

def geoip():
    global _geoip
    if _geoip is None and HAS_GEOIP:
        from django.contrib.gis.geoip import GeoIP
        try:
            _geoip = GeoIP()
        except Exception as e:
            warnings.warn(str(e))
    return _geoip

