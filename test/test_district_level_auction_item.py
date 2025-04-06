from src.district_level_garden.auction_item import AuctionItem

def test_auction_item():
    item = AuctionItem(
    item_no:= 10,
    description:= 'desc',
    value=23.5,
    minimum_bid=0.5,
    donor='someone',
    increment= 2.5,
    title = 'some title',
    live_auction= False,
    buy_now=False,
    split_bid=False,
    section='some section'
    )
