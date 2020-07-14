import datetime
import os
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

from models import MeasuringData, MeasuringStands


engine = create_engine(os.environ.get('DATABASE_URL'), echo=True)

Session = sessionmaker(bind=engine)
session = Session()


def periodic_load():
    measuring_stands = session.query(MeasuringStands).all()
    for measuring_stand in measuring_stands:
        data_json = requests.get(
            "http://api.gios.gov.pl/pjp-api/rest/data/getData/{}".format(
                measuring_stand.id
            )
        ).json()
        if data_json["values"]:
            data = data_json["values"][1]
            measure_data = MeasuringData(
                value=data["value"],
                date=datetime.datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S"),
                sensor_id=measuring_stand.id,
                sensor=measuring_stand,
            )
            session.add(measure_data)

            session.commit()


if __name__ == "__main__":
    while True:
        time.sleep(3600)
        periodic_load()
