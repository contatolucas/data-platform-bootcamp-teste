#!/usr/bin/env python3

#from athena.stack import AthenaStack
from aws_cdk import core

from data_platform_bootcamp_teste.data_lake.stack import DataLakeStack
from common_stack import CommonStack
from glue_catalog.stack import GlueCatalogStack

app = core.App()
data_lake = DataLakeStack(app)
#athena = AthenaStack(app)
#glue = GlueCatalogStack(app, data_lake_bucket=data_lake.data_lake_raw_bucket)
#common = CommonStack(app)
app.synth()