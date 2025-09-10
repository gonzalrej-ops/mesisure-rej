import dlt


# Please edit the sample below


@dlt.table
def gold_layerpipeline():
    return spark.read.table("samples.nyctaxi.trips")