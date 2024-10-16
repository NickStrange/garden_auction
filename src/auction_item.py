import math
from dataclasses import dataclass
import pandas as pd


@dataclass
class AuctionItem:
    item_no: int
    description: str
    value: float
    minimum_bid: float
    donor: str
    increment: float
    title: str

    def __post_init__(self):
        if str(self.value) == 'nan':
            self.value=100
        else:
            self.value=int(self.value)
        if str(self.minimum_bid) =='nan':
            self.minimum_bid = int(self.value*0.5)
        if str(self.title) =='nan':
            self.title=''


    def is_valid(self):
        return str(self.description) != 'nan'




