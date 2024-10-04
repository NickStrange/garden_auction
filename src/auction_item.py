from dataclasses import dataclass


@dataclass
class AuctionItem:
    item_no: int
    description: str
    value: float
    minimum_bid: float
    donor: str
    increment: float
    title: str



