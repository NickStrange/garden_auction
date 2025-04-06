import math
from dataclasses import dataclass


@dataclass
class AuctionItem:
    item_no: int = 0
    donor: str = ''
    title: str = ''
    value: float = float(0)
    minimum_bid: float = float(5)
    increment: float = float(5)
    description: str = None

    def __post_init__(self):
        if self.value != '':
            if str(self.value) == 'nan':
                self.value=0
            else:
                self.value=int(self.value)
        if str(self.description) == 'nan':
            self.description=''
        if str(self.minimum_bid) == 'nan':
            self.minimum_bid = 0
        if self.minimum_bid == 0:
            self.minimum_bid = int(self.value*0.5)
        if str(self.title) == 'nan':
            self.title = ''
        if self.value != '':
            self.increment = 2 if self.value <= 15 else 5
