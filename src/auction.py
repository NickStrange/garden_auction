from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from paragraph1 import gen_header_table
from src.auction_item import AuctionItem
from src.bid import set_bid_info
from src.description import set_description
from src.table import set_table
from src.title import set_title
import pandas as pd

def footer(item: AuctionItem) -> str:
    def decode(label: str, value:str) -> str:
        if value == 'Y':
            return f'{label}'
        return ''

    buy_now = '' if not item.buy_now else f' BUY NOW FOR ${item.buy_now}'
    items=[]
    if item.section:
        items.append(item.section)
    if item.live_auction == 'Y':
        items.append(decode("live auction", item.live_auction))
    if item.split_bid == 'Y':
        items.append(decode("split bid", item.split_bid))
    return "\n     "+": ".join(items)


def front_page(item: AuctionItem, pdf):
    width, height = A4
    heightlist = [
                  0.05 *height,
                  0.1*height, #title
                  0.25*height,  #description
                  0.50*height, #table
                  0.025 * height,  # buy now
                  0.075 *height, #footer
                  ]
    buy_now = '' if not item.buy_now else f'Bidder # ____ Bidder_name __________Buy now for ${item.buy_now}'
    mainTable = Table([
        [''],
        [set_title(width, heightlist[1])],
        [set_description(width, heightlist[2], item)],
        [set_table(width, heightlist[3], item)],
        [buy_now],
        [footer(item)],
    ], colWidths=width,
       rowHeights=heightlist)

    mainTable.setStyle([
    #    ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (0, -1), 0),
    #flowers
        ('BOTTOMPADDING', (0, 0), (0, 0), 15),
    #description
        ('BOTTOMPADDING', (0, 1), (0, 1), 10),
    #Table
        ('ALIGN', (0, 3), (0, 3), 'CENTRE'),
        ('VALIGN', (0, 3), (0, 3), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 4), (-1, -1), 0),
    #buy_now
        ('ALIGN', (0, 4), (0, 4), 'CENTRE'),
        ('FONTSIZE', (0, 4), (0, 4), 20),
    #footer
        ('VALIGN', (0, 5), (0, 5), 'TOP'),
    ])

    mainTable.wrapOn(pdf, 0, 0)
    mainTable.drawOn(pdf, 0, 0)

def produce_item_page(item:AuctionItem):
    item_no = f'{item.item_no:03d}' if item.item_no !='' else 999
 #   pdf = canvas.Canvas(f"../data/items/auction{item_no}.pdf", pagesize=A4)
    front_page(item, pdf)
 #   pdf.showPage()
# back_page(item, pdf)
# pdf.showPage()
 #   pdf.save()

def read_file(file:str):
    items_df = (pd.read_excel(file)
                  .sort_values('Item Description Size')
                  .reset_index(drop=True))
    print(items_df.tail())
    return items_df


if __name__ == '__main__':
    items = read_file('../data/IG_1-12.xlsx')
    pdf = canvas.Canvas(f"../data/items/auction_items.pdf", pagesize=A4)
    saved = None
    for index, item_row in items.iterrows():
        item = AuctionItem(item_no=index+1,
                   description=item_row['Item Description Size'],
                   value=item_row['Retail Value'],
                   minimum_bid=item_row['Opening Bid'], #50%
                   increment=5,
                   donor=item_row['Donor'],
                   title=item_row['Title'],
                   live_auction=item_row['Live Auction'],
                   split_bid=item_row['Split Bid'],
                   buy_now=item_row['Buy Now'],
                   section=item_row['Section'],
        )
       # if item.is_valid():
        saved=item
        front_page(item, pdf)
        produce_item_page(item)

        pdf.showPage()
    for row in range(15):
        front_page(saved, pdf)
        pdf.showPage()
    pdf.save()
