from flask_migrate import Migrate

from app import create_app, db
from models import (
    MeasuringStation,
    City,
    CitySchema,
    MeasuringStationSchema,
    MeasuringStands,
    MeasuringData,
    IndexQuality,
)

app = create_app()
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        City=City,
        MeasuringStation=MeasuringStation,
        CitySchema=CitySchema,
        MeasuringStationSchema=MeasuringStationSchema,
        MeasuringStands=MeasuringStands,
        MeasuringData=MeasuringData,
        IndexQuality=IndexQuality,
    )
