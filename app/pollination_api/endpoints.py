from flask_restful import Resource
from sqlalchemy import or_
from models import (
    City,
    MeasuringStation,
    MeasuringStationSchema,
    MeasuringStands,
    MeasuringStandsSchema,
    MeasuringData,
    MeasuringDataSchema,
    IndexQuality,
    IndexQualitySchema,
)
from . import api


class Stations(Resource):
    def get(self):
        stations = MeasuringStation.query.all()
        stations_schema = MeasuringStationSchema(many=True)

        return stations_schema.dump(stations)


class CityStations(Resource):
    def get(self, name):
        cities = City.query.filter(
            or_(
                City.name.ilike(name),
                City.commune_name.ilike(name),
                City.district_name.ilike(name),
                City.province_name.ilike(name),
            )
        ).all()

        stations = [
            MeasuringStation.query.filter_by(city_id=city.id).first() for city in cities
        ]
        stations_schema = MeasuringStationSchema(many=True)

        return stations_schema.dump(stations), 200 if cities else 404


class MeasuringStandsList(Resource):
    def get(self, _id):
        measuring_stands = MeasuringStands.query.filter_by(station_id=_id).all()
        measuring_stands_schema = MeasuringStandsSchema(many=True)

        return (
            measuring_stands_schema.dump(measuring_stands),
            200 if measuring_stands else 404,
        )


class MeasuringDataList(Resource):
    def get(self, _id):
        measuring_data = (
            MeasuringData.query.filter_by(sensor_id=_id)
            .order_by(MeasuringData.date.desc())
            .limit(24)
            .all()
        )
        measuring_data_schema = MeasuringDataSchema(many=True)

        return (
            measuring_data_schema.dump(measuring_data),
            200 if measuring_data else 404,
        )


class QualityIndicators(Resource):
    def get(self, _id):
        index_quality = IndexQuality.query.filter_by(id=_id).first()
        index_quality_schema = IndexQualitySchema()

        return index_quality_schema.dump(index_quality), 200 if index_quality else 404


api.add_resource(CityStations, "/cities-stations/<string:name>")
api.add_resource(Stations, "/stations")
api.add_resource(MeasuringStandsList, "/measuring-stands/<int:_id>")
api.add_resource(QualityIndicators, "/quality-indicators/<int:_id>")
api.add_resource(MeasuringDataList, "/measuring-data/<int:_id>")
