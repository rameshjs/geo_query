from django.shortcuts import render
import geoip2.database


def index(request):
    with geoip2.database.Reader("GeoLite2-ASN.mmdb") as reader:
        response = reader.asn("223.178.84.220")
        print(response)
    return
