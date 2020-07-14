import requests
import datetime
from models import City, MeasuringStation, MeasuringData, MeasuringStands, IndexQuality
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(os.environ.get('DATABASE_URL'), echo=True)

Session = sessionmaker(bind=engine)
session = Session()


def load_quality_index():
    index = {
        "PM10": [21, 61, 101, 141, 201],
        "PM2.5": [13, 37, 61, 85, 121],
        "O3": [71, 121, 151, 181, 241],
        "NO2": [41, 101, 151, 201, 401],
        "SO2": [51, 101, 201, 351, 501],
        "C6H6": [6, 11, 16, 21, 51],
        "CO": [3000, 7000, 11000, 15000, 21000],
    }
    for name in index.keys():
        index_quality = IndexQuality(
            name=name,
            bad=index[name][4],
            sufficient=index[name][3],
            moderate=index[name][2],
            good=index[name][1],
            very_good=index[name][0],
        )
        session.add(index_quality)

    session.commit()


def load_stations_data():
    stations = requests.get(
        "http://api.gios.gov.pl/pjp-api/rest/station/findAll"
    ).json()

    for station in stations:
        city = City(
            name=station["city"]["name"],
            commune_name=station["city"]["commune"]["communeName"],
            district_name=station["city"]["commune"]["districtName"],
            province_name=station["city"]["commune"]["provinceName"],
        )
        session.add(city)
        session.add(
            MeasuringStation(
                id=station["id"],
                name=station["stationName"],
                gegrLat=station["gegrLat"],
                gegrLon=station["gegrLon"],
                city_id=station["city"]["id"],
                city=city,
            )
        )

    session.commit()


def load_measurement_data():
    # MeasuringStation

    stations = session.query(MeasuringStation).all()

    # MeasuringStands
    quality_indexes = session.query(IndexQuality).all()
    for station in stations:
        data_list = requests.get(
            "http://api.gios.gov.pl/pjp-api/rest/station/sensors/{}".format(station.id)
        ).json()
        for data in data_list:
            measuring_stand = MeasuringStands(
                id=data["id"],
                name=data["param"]["paramName"],
                code=data["param"]["paramCode"],
                station_id=station.id,
                station=station,
            )

            for quality_index in quality_indexes:
                if quality_index.name == measuring_stand.code:
                    measuring_stand.index = quality_index
                    measuring_stand.index_id = quality_index.id
                    session.add(measuring_stand)

    session.commit()

    # MeasuringData

    measuring_stands = session.query(MeasuringStands).all()
    for measuring_stand in measuring_stands:
        data_json = requests.get(
            "http://api.gios.gov.pl/pjp-api/rest/data/getData/{}".format(
                measuring_stand.id
            )
        ).json()
        for data in data_json["values"]:
            measure_data = MeasuringData(
                value=data["value"],
                date=datetime.datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S"),
                sensor_id=measuring_stand.id,
                sensor=measuring_stand,
            )
            session.add(measure_data)

    session.commit()


if __name__ == "__main__":
    load_stations_data()
    load_quality_index()
    load_measurement_data()
