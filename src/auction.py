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
    items=[]
    if item.section:
        items.append(item.section)
    if item.live_auction == 'Y':
        items.append(decode("live auction", item.live_auction))
    if item.buy_now == 'Y':
        items.append(decode("buy now", item.buy_now))
    if item.split_bid == 'Y':
        items.append(decode("split bid", item.split_bid))
    return ": ".join(items)


def front_page(item: AuctionItem, pdf):
    width, height = A4
    heightlist = [0.1*height, #title
                  0.3*height,  #description
                  0.57*height, #table
                  0.03 *height
                  ]

    mainTable = Table([
        [set_title(width, heightlist[0])],
        [set_description(width, heightlist[1], item)],
        [set_table(width, heightlist[2], item)],
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
        ('ALIGN', (0, 2), (0, 2), 'CENTRE'),
        ('VALIGN', (0, 2), (0, 2), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 2), (-1, -1), 0),
    ])

    mainTable.wrapOn(pdf,0,0)
    mainTable.drawOn(pdf, 0, 0)

def back_page(item: AuctionItem, pdf):
    width, height = A4
    heightlist =[height*0.025, height*0.95, height*0.025]
    backTable = Table([
        'fff',
        [set_table(width, heightlist[1], item, front=False)],
        'ggg'
    ], colWidths=width,
       rowHeights=heightlist)
    backTable.setStyle([
    #    ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (0, -1), 0),
   #     ('BOTTOMPADDING', (0, 0), (-1, -1), 15),

        ('ALIGN', (0, 1), (0, 1), 'CENTRE'),
        ('VALIGN', (0, 1), (0, 1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ])
    backTable.wrapOn(pdf,0,0)
    backTable.drawOn(pdf, 0, 0)
    return backTable

def produce_item_page(item:AuctionItem):
    pdf = canvas.Canvas(f"../data/items/auction{item.item_no:03d}.pdf", pagesize=A4)
    front_page(item, pdf)
    pdf.showPage()
# back_page(item, pdf)
# pdf.showPage()
    pdf.save()

def read_file(file:str):
    items_df = (pd.read_excel(file)
                  .sort_values('Live Auction')
                  .reset_index(drop=True))
    print(items_df.tail())
    return items_df


if __name__ == '__main__':
    items = read_file('../data/IG_8.xlsx')
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
        if item.is_valid():
            produce_item_page(item)
