# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.orm import declarative_base

from zvt.contract.register import register_schema
from zvt.domain.quotes import FutureKdataCommon

KdataBase = declarative_base()


class Future1dKdata(KdataBase, FutureKdataCommon):
    __tablename__ = "future_1d_kdata"


register_schema(providers=["em"], db_name="future_1d_kdata", schema_base=KdataBase, entity_type="future")

# the __all__ is generated
__all__ = ["Future1dKdata"]
