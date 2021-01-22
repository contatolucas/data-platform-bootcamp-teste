#!/usr/bin/env python3

from athena.stack import AthenaStack
from aws_cdk import core

from data_platform_bootcamp_teste.data_lake.stack import DataLakeStack
from glue_catalog.stack import GlueCatalogStack
#from common_stack import CommonStack

app = core.App()
data_lake = DataLakeStack(app)
glue = GlueCatalogStack(app, data_lake_bucket=data_lake.data_lake_raw_bucket)
athena = AthenaStack(app)
#common = CommonStack(app)
app.synth()