from fastapi import Query
from pydantic import BaseModel
from decimal import Decimal
import re

class CalcMortgageGetRequest(BaseModel):
    amount: Decimal = None
    down_payment: Decimal = None
    mortage_type: int = None
    intrest_rate: Decimal = None
    property_tax: Decimal = None
    annual_insurance: Decimal = None
    HOA: Decimal = None
    PMI: Decimal = None

class CalcMortgageResponse(BaseModel):
    pi: Decimal = None
    property_taxes: Decimal = None
    HOA: Decimal = None
    PMI: Decimal = None
    total: Decimal = None

