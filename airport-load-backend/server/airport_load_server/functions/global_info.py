from airport_load_server.functions.connection import PgPool, fetch_all_query
from airport_load_server.models import GlobalLoadInfo, BriefAirportLoadInfo
import csv


async def get_global_load():
    data = []
    with open('airport_load_server/functions/mock_load.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    result = []
    for d in data:
        item = BriefAirportLoadInfo(
            airport_code=d['departure_airport'],
            pax_load=d['count'],
            latitude=d['LATITUDE'],
            longititude=d['LONGITUDE']
        )
        result.append(item)
    return GlobalLoadInfo(data=result)
