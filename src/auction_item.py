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
    live_auction: str
    buy_now :str
    split_bid :str
    section :str

    def __post_init__(self):
        if str(self.value) == 'nan':
            self.value=100
        else:
            self.value=int(self.value)
        if str(self.minimum_bid) =='nan':
            self.minimum_bid = int(self.value*0.5)
        else:
            self.minimum_bid = int(self.minimum_bid)
        if str(self.title) =='nan':
            self.title=''
        if str(self.section) == 'nan':
            self.section = ''
        if self.value <= 19:
            self.increment=2
        if self.live_auction == 'nan':
                self.live_auction = ''
        if str(self.description) == 'nan':
            self.description = '  '
            self.value='   '
            self.title=''
            self.minimum_bid='   '
            self.increment='   '
            self.item_no=''
            self.donor=''
            self.section = '          '
        else:
            self.description = str(self.description).replace("_x000D_", "<br />")
        buy_now = [0, 175, 190,50,250,100,95,80, 8]
        if str(self.buy_now) == 'nan':
            self.buy_now = ''
        else:
            self.buy_now = buy_now[int(self.buy_now)]
      #  if self.buy_now =='Y':
      #      self.buy_now = int(self.value*1.1)
      #  else:
      #      self.buy_now = ''

    def is_valid(self):
        return str(self.description) != 'nan'




