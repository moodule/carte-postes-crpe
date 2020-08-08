# -*- coding: utf-8 -*-

"""
====
CRPE
====

Maps all the job offers and rank them.
Designed to help choose the best position you're likely to
get out of 100s.
"""

from __future__ import division, print_function, absolute_import

import pprint
import requests

import googlemaps

#####################################################################
# PRINTER
#####################################################################

PP = pprint.PrettyPrinter(indent=4)

#####################################################################
# GMAPS API
#####################################################################

KEY = ""
with open("gmap_api-key.txt", "r") as __file:
    KEY = __file.readline()

#####################################################################
# SCHOOLS
#####################################################################

ECOLES = [
    "BAYON,+Ecole+primaire+F.+Dolto",
    "FLAVIGNY+S+MOSELLE,+ecole+primaire+village",
    "MAGNIERES,+ecole+primaire",
    "DAMELEVIERES+Louis+Aragon+élémentaire",
    "AZERAILLES,+ecole+primaire",
    "PIENNES,+Ecole+primaire+J+Zay",
    "AUDUN+LE+ROMAN+Ecole+primaire+F.+Poulbot",
    "MANCIEULLES+VAL+DE+BRIEY,+Ecole+primaire+Hervé+Bazin",
    "VALLEROY,+ecole+primaire,+Emile+Duhamel",
    "PIENNES,+Ecole+primaire+Elsa.+Triolet",
    "MARS+LA+TOUR,+ecole+primaire+aire+Albert+Lebrun",
    "HOMECOURT,+Ecole+primaire+H.+Defaut",
    "JARNY,+ecole+primaire+Jules+Ferry+(mat)",
    "ROSIERES+AUX+SALINES,+ecole+primaire",
    "DOMBASLE,+Ecole+primaire+J.+L'hôte",
    "JARVILLE,+Ecole+primaire+L.+Majorelle",
    "JARVILLE,+Ecole+primaire+Florian",
    "LANEUVEVILLE+DVT+NANCY,+Ecole+primaire+Montaigu",
    "LANEUVEVILLE+DVT+NANCY,+Ecole+primaire+du+Centre",
    "LANEUVEVILLE+DVT+NANCY,+Ecole+primaire+Montaigu",
    "ROSIERES+AUX+SALINES,+Mat",
    "ST+NICOLAS+DE+PORT,+Ecole+primaire+P+et+M+Curie",
    "ST+NICOLAS+DE+PORT,+Ecole+primaire+P.+Castel",
    "ST+NICOLAS+DE+PORT,+Ecole+primaire+P.+Castel",
    "VILLE+EN+VERMOIS,+ecole+primaire+Sonnini",
    "ST+NICOLAS+DE+PORT,+Ecole+primaire+J.+Moulin",
    "JARVILLE,+Ecole+primaire+Calmette+et+Guérin",
    "LONGWY,+ecole+primaire+Chadelle",
    "LONGWY,+ecole+primaire+Chadelle",
    "LONGWY,+Ecole+primaire+Dartein",
    "MONT+ST+MARTIN,+Ecole+primaire+J.+Macé",
    "CONS+LA+GRANDVILLE,+ecole+primaire+",
    "HERSERANGE+Ecole+primaire+J.+Simon",
    "LEXY,+Ecole+primaire+J.+Macé",
    "MORFONTAINE,+ecole+primaire+G.+Sand",
    "REHAINVILLER,+ecole+primaire",
    "LUNEVILLE,+Demangeot+Elem",
    "CIREY+SUR+VEZOUZE,+Elem",
    "LUNEVILLE,+Alsace+Maternelle",
    "NANCY,+Ecole+primaire+Boudonville",
    "NANCY,+Ecole+primaire+Braconnot",
    "NANCY,+Ecole+primaire+Braconnot",
    "NANCY,+Ecole+primaire+Braconnot",
    "NANCY,+Ecole+primaire+Didion+Raugraff",
    "NANCY,+Ecole+primaire+3+Maisons",
    "NANCY,+Ecole+primaire+3+Maisons",
    "NANCY,+Ecole+primaire+A.+Mézières",
    "NANCY,+Ecole+primaire+Boudonville",
    "NANCY,+Ecole+primaire+Charles+3",
    "NANCY,+Ecole+primaire+Didion",
    "NANCY,+Ecole+primaire+Gallé",
    "30 Rue Emile Gebhart, 54000 Nancy, France",
    "NANCY,+Ecole+primaire+3+Maisons",
    "NANCY,+Ecole+primaire+3+Maisons",
    "NANCY,+Ecole+primaire+M.+Leroy",
    "NANCY,+Ecole+primaire+Stanislas",
    "NANCY,+Ecole+primaire+Boudonville",
    "NANCY,+Ecole+primaire+Boudonville",
    "NANCY,+Ecole+primaire+Braconnot",
    "NANCY,+Ecole+primaire+Roberty",
    "NANCY,+Ecole+primaire+3+Maisons",
    "NANCY,+Ecole+primaire+Stanislas",
    "LAXOU+Ecole+primaire+V.Hugo",
    "MAXEVILLE+Ecole+primaire+Vautrin",
    "LAXOU+Ecole+primaire+V.Hugo",
    "NANCY+Ecole+primaire+Charlemagne",
    "NANCY+BEAUREGARD+ecole+primaire",
    "MAXEVILLE+Ecole+primaire+Vautrin",
    "MAXEVILLE+Ecole+primaire+Vautrin",
    "MAXEVILLE+Ecole+primaire+Vautrin",
    "LAXOU+Ecole+primaire+Pergaud",
    "NANCY+Ecole+primaire+Charlemagne",
    "NANCY+Ecole+primaire+Charlemagne",
    "LAXOU+Ecole+primaire+Zola",
    "MAXEVIILE+Ecole+primaire+Vautrin",
    "LAXOU+Ecole+primaire+Zola",
    "LAXOU+Ecole+primaire+Zola",
    "BOUXIERES+AUX+DAMES,+Ecole+primaire+Thibault",
    "FAULX,+ecole+primaire+Les+Marronniers",
    "CHAMPIGNEULLES,+Ecole+primaire+J.+Moulin",
    "CHAMPIGNEULLES,+ecole+primaire+Buffon+",
    "CHAMPIGNEULLES,+Ecole+primaire+J.+Moulin",
    "MALZEVILLE,+Ecole+primaire+P.+Bert",
    "EULMONT,+Ecole+primaire+Les+Vignottes",
    "LIVERDUN+Ecole+primaire+Rond+Chêne",
    "MALLELOY,+Ecole+primaire",
    "MALZEVILLE,+Ecole+primaire+Geny",
    "CUSTINES,+Ecole+primaire+Centre",
    "LIVERDUN,+Ecole+primaire+Rond+Chêne",
    "DIEULOUARD,+ecole+primaire+",
    "JEANDELAINCOURT,+ecole+primaire",
    "MARBACHE,+ecole+primaire+",
    "PAGNY+SUR+MOSELLE,+Ecole+primaire+P.+Bert",
    "PONT+A+MOUSSON,+Ecole+primaire+P.+Dohm",
    "PONT+A+MOUSSON,+Ecole+primaire+St+Jean",
    "PONT+A+MOUSSON,+Ecole+primaire+St+Martin",
    "BRIN+S+SEILLE,+ecole+primaire",
    "CHAMPENOUX,+ecole+primaire",
    "CHAMPENOUX,+ecole+primaire",
    "ESSEY+LES+NANCY,+Ecole+primaire+Centre",
    "ESSEY+LES+NANCY,+Ecole+primaire+Centre",
    "ESSEY+LES+NANCY,+Ecole+primaire+Mouzimpré",
    "ESSEY+LES+NANCY,+ecole+primaire+Prevert",
    "SEICHAMPS+ecole+primaire+L+Michel",
    "TOMBLAINE,+Ecole+primaire+Brossolette",
    "TOMBLAINE,+Ecole+primaire+Brossolette",
    "FOUG,+Ecole+primaire+Luton",
    "DOMMARTIN+LES+TOUL,+Ecole+primaire+J.+Ferry",
    "TOUL,+Ecole+primaire+La+Sapinière",
    "24 Rue de l'Abbé Lenfant, 54115 Favières, France",
    "COLOMBEY+LES+BELLES,+ecole+primaire",
    "COLOMBEY+LES+BELLES,+ecole+primaire",
    "VILLEY+SAINT+ETIENNE+ecole+primaire",
    "MENIL+LA+TOUR,+ecole+primaire",
    "TOUL,+Ecole+primaire+Les+Eglantines",
    "TOUL,+ecole+primaire+Saint+Evre",
    "FOUG,+Ecole+primaire+Les+Tilleuls",
    "DOMEVRE+EN+HAYE,+ecole+primaire",
    "VANNES+LE+CHATEL,+ecole+primaire",
    "ALLAIN,+ecole+primaire",
    "VANDOEUVRE,+Ecole+primaire+Europe+Nations",
    "VANDOEUVRE,+Ecole+primaire+Europe+Nations",
    "VANDOEUVRE,+Ecole+primaire+Charmois",
    "VANDOEUVRE,+Ecole+primaire+Charmois",
    "VANDOEUVRE,+Ecole+primaire+Brossolette",
    "LUDRES,+Ecole+primaire+J+Prévert",
    "VANDOEUVRE,+Ecole+primaire+Brabois",
    "VANDOEUVRE,+Ecole+primaire+Bert",
    "LUDRES,+Ecole+primaire+J.+Prévert",
    "VANDOEUVRE,+Ecole+primaire+J.+Macé",
    "VANDOEUVRE,+Ecole+primaire+J.+Pompey",
    "LUDRES,+Ecole+primaire+P.+Loti",
    "MAIZIERES,+primaire+Emile+Gallé",
    "VILLERS+LES+NANCY,+Ecole+primaire+des+Aiguillettes",
    "VILLERS+LES+NANCY,+Ecole+primaire+des+Aiguillettes",
    "SEXEY+AUX+FORGES,+ecole+primaire",
    "VELAINE,+Ecole+primaire",
    "NEUVES+MAISONS,+Ecole+primaire+E.+Zola",
    "XIROCOURT,+primaire+du+Madon",
    "VEZELISE,+maternelle",
    "VILLERS+LES+NANCY,+ecole+primaire+du+Château",
    "DIARVILLE,+ecole+primaire",
    "CHALIGNY,+Ecole+primaire+Banvoie",
    "VILLERS+LES+NANCY,+Ecole+primaire+A.+Camus",
    "VILLERS+LES+NANCY,+Ecole+primaire+Camus",
    "7 Lotissement Echo, 54740 Benney"]

DESTINATION = "54b Boulevard de Scarpone, 54000 Nancy"

#####################################################################
# LOCALIZATION
#####################################################################

_gmaps_client = googlemaps.Client(key=KEY)
_addresses = []
_geolocations = []
_distances = []
_durations = []

for _ecole in ECOLES:
    _loc = _gmaps_client.geocode(_ecole, components={"country": "FR", "administrative_area_level_1": "Grand+Est"})
    _dist = _gmaps_client.distance_matrix(_ecole, DESTINATION)
    # address
    if len(_loc):
        _addresses.append(_loc[0]["formatted_address"])
        _geolocations.append(_loc[0]["geometry"]["location"])
    else:
        _addresses.append("?")
        _geolocations.append({'lat': 48.7, 'lng': 6.16}) # INSPE
    # distance
    if _dist:
        _distance_details = _dist['rows'][0]['elements'][0]
        if "distance" in _distance_details.keys():
            _distances.append(_distance_details["distance"]["value"] * 0.001)
        else:
            _distances.append(-10)
        if "duration" in _distance_details.keys():
            _durations.append(_distance_details["duration"]["value"] / 60.)
        else:
            _durations.append(-10)
    else:
        _distances.append(-10)
        _durations.append(-10)

#####################################################################
# EXPORT
#####################################################################

with open("addresses.csv", "w") as _file:
    for _a in _addresses:
        _file.write("{}\n".format(_a))

with open("distances.csv", "w") as _file:
    for _d in _distances:
        _file.write("{}\n".format(round(_d, 1))) # in km

with open("durations.csv", "w") as _file:
    for _d in _durations:
        _file.write("{}\n".format(round(_d, 0))) # in minutes

with open("geolocations.csv", "w") as _file:
    for _g in _geolocations:
        _file.write("{};{}\n".format(
            round(_g.get("lat", 48.7), 4),
            round(_g.get("lng", 6.16), 4)))
