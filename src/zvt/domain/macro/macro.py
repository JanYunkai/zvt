# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Float, BIGINT
from sqlalchemy.orm import declarative_base

from zvt.contract import Mixin
from zvt.contract.register import register_schema

MacroBase = declarative_base()


class Economy(MacroBase, Mixin):
    """
    宏观经济
    """
    # https://datatopics.worldbank.org/world-development-indicators//themes/economy.html
    __tablename__ = "economy"

    code = Column(String(length=32))
    name = Column(String(length=32))
    # 人口
    population = Column(BIGINT)
    # 国内生成总值
    gdp = Column(Float)
    # 人均国内生成总值
    gdp_per_capita = Column(Float)
    # 
    gdp_per_employed = Column(Float)
    # gdp增长
    gdp_growth = Column(Float)
    # 农业增长
    agriculture_growth = Column(Float)
    # 行业增长
    industry_growth = Column(Float)
    # 制造增长
    manufacturing_growth = Column(Float)
    # 服务增长
    service_growth = Column(Float)
    # 消费增长
    consumption_growth = Column(Float)
    # 资本增长
    capital_growth = Column(Float)
    # 出口增长
    exports_growth = Column(Float)
    # 进口增长
    imports_growth = Column(Float)
    # 国民总收入：是指国内生成总值（GDP）加上来自国外的要素收入再减去对国外的要素支出
    # 国民总收入 = 国内生成总值 + （来自国外的要素收入-对国外的要素支出）
    gni = Column(Float)
    # 人均国民总收入
    gni_per_capita = Column(Float)
    # 总储蓄
    gross_saving = Column(Float)
    # 居民消费价格指数（consumer price index）
    cpi = Column(Float)
    # 失业率
    unemployment_rate = Column(Float)
    # 国内生产总值的外国直接投资
    fdi_of_gdp = Column(Float)


register_schema(providers=["wb"], db_name="macro", schema_base=MacroBase)
# the __all__ is generated
__all__ = ["Economy"]
