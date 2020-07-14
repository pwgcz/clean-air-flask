from app import db, ma


class City(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    commune_name = db.Column(db.String(64))
    district_name = db.Column(db.String(64))
    province_name = db.Column(db.String(64))

    def __repr__(self):
        return "<City: {}, Id: {}>".format(self.name, self.id)


class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City


class MeasuringStation(db.Model):
    __tablename__ = "stations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    gegrLat = db.Column(db.Float)
    gegrLon = db.Column(db.Float)
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id"))
    city = db.relationship("City", backref="station", uselist=False)

    def __iter__(self):
        return "<MeasuringStation: {}, Id: {}>".format(self.name, self.id)


class MeasuringStationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MeasuringStation
        include_fk = True


class IndexQuality(db.Model):
    __tablename__ = "indexes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    bad = db.Column(db.Integer)
    sufficient = db.Column(db.Integer)
    moderate = db.Column(db.Integer)
    good = db.Column(db.Integer)
    very_good = db.Column(db.Integer)

    def __repr__(self):
        return "<IndexQuality name:{}>".format(self.name)


class IndexQualitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = IndexQuality


class MeasuringStands(db.Model):
    __tablename__ = "sensors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    code = db.Column(db.String(64))

    index_id = db.Column(db.Integer, db.ForeignKey("indexes.id"))
    index = db.relationship("IndexQuality", backref="sensors")

    station_id = db.Column(db.Integer, db.ForeignKey("stations.id"))
    station = db.relationship("MeasuringStation", backref="sensors")

    def __repr__(self):
        return "<Sensor: {}>".format(self.name)


class MeasuringStandsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MeasuringStands
        include_fk = True


class MeasuringData(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    value = db.Column(db.Float)
    sensor_id = db.Column(db.Integer, db.ForeignKey("sensors.id"))
    sensor = db.relationship("MeasuringStands", backref="data")

    def __repr__(self):
        return "<Data: {}, value: {}>".format(self.date, self.value)


class MeasuringDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MeasuringData
        include_fk = True
