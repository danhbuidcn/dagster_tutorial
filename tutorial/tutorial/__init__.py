from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    EnvVar,
)

from .resources import DataGeneratorResource
from . import assets

all_assets = load_assets_from_modules([assets])

# Define a job that will materialize the assets
hackernews_job = define_asset_job("hackernews_job", selection=AssetSelection.all())

# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
hackernews_schedule = ScheduleDefinition(
    job=hackernews_job,
    cron_schedule="0 * * * *",  # every hour
)

# Configure the resource with an environment variable here
datagen = DataGeneratorResource(
    num_days=EnvVar.int("HACKERNEWS_NUM_DAYS_WINDOW")
)  # Make the resource, default 7 days

defs = Definitions(
    assets=all_assets,
    schedules=[hackernews_schedule],
    resources={
        "hackernews_api": datagen,  # Add the newly-made resource here
    },
)