from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from src.district_level_garden.auction_item import AuctionItem
from src.district_level_garden.description import set_description
from src.district_level_garden.table import set_table
from src.district_level_garden.title import set_title
import pandas as pd


def footer(item: AuctionItem) -> str:
    """
    :param item:
    :return:
    """
    """ add live auctio label etc to footer"""
    def decode(label: str, value: str) -> str:
        if value == 'Y':
            return f'{label}'
        return ''

    items: list = []
    if item.section:
        items.append(item.section)
    if item.live_auction == 'Y':
        items.append(decode("live auction", item.live_auction))
    if item.split_bid == 'Y':
        items.append(decode("split bid", item.split_bid))
    return "\n     "+": ".join(items)


def front_page(item: AuctionItem, pdf):
    width, height = A4
    height_list = [
                  0.05 * height,
                  0.1 * height,    # title
                  0.25 * height,   # description
                  0.50 * height,   # table
                  0.025 * height,  # buy now
                  0.075 * height,  # footer
                  ]
    buy_now = '' if not item.buy_now else f'Bidder # ____ Bidder_name __________Buy now for ${item.buy_now}'
    main_table = Table([
        [''],
        [set_title(width, height_list[1])],
        [set_description(width, height_list[2], item)],
        [set_table(width, height_list[3], item)],
        [buy_now],
        [footer(item)],
    ], colWidths=width,
       rowHeights=height_list)

    main_table.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (0, -1), 0),
        # flowers
        ('BOTTOMPADDING', (0, 0), (0, 0), 15),
        # description
        ('BOTTOMPADDING', (0, 1), (0, 1), 10),
        # Table
        ('ALIGN', (0, 3), (0, 3), 'CENTRE'),
        ('VALIGN', (0, 3), (0, 3), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 4), (-1, -1), 0),
        # buy_now
        ('ALIGN', (0, 4), (0, 4), 'CENTRE'),
        ('FONTSIZE', (0, 4), (0, 4), 20),
        # footer
        ('VALIGN', (0, 5), (0, 5), 'TOP'),
    ])

    main_table.wrapOn(pdf, 0, 0)
    main_table.drawOn(pdf, 0, 0)


def produce_item_page(item: AuctionItem):
    front_page(item, canvas)


def read_file(file: str):
    items_df = (pd.read_excel(file)
                  .sort_values('Item Description Size')
                  .reset_index(drop=True))
    print(items_df.tail())
    return items_df


if __name__ == '__main__':
    print('reading+++++++++++++')
    all_items = read_file('../data/IG_1-12.xlsx')
    canvas = canvas.Canvas(f"./garden/items/auction_items.pdf", pagesize=A4)
    saved = None
    for index, item_row in all_items.iterrows():
        used_item = AuctionItem(item_no=index+1,
                                description=item_row['Item Description Size'],
                                value=item_row['Retail Value'],
                                minimum_bid=item_row['Opening Bid'],  # 50%
                                increment=5,
                                donor=item_row['Donor'],
                                title=item_row['Title'],
                                live_auction=item_row['Live Auction'],
                                split_bid=item_row['Split Bid'],
                                buy_now=item_row['Buy Now'],
                                section=item_row['Section']
                                )
        saved = used_item
        front_page(used_item, canvas)
        produce_item_page(used_item)

        canvas.showPage()
    for row in range(15):
        front_page(saved, canvas)
        canvas.showPage()
    canvas.save()
