from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from src.district_level_garden.auction_item import AuctionItem
from src.district_level_garden.description import set_description
from src.district_level_garden.table import set_table
from src.district_level_garden.title import set_title
import pandas as pd

def front_page(item: AuctionItem, pdf):
    width, height = A4
    height_list = [
                  0.05 * height,
                  0.1 * height,    # title
                  0.25 * height,   # description
                  0.6 * height,   # table
                  0.025 * height,  # footer
                  ]
    main_table = Table([
        [''],
        [set_title(width, height_list[1])],
        [set_description(width, height_list[2], item)],
        [set_table(width, height_list[3], item)],
        [],
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


def produce_item_page(item: AuctionItem, canv):
    front_page(item, canv)


def read_file(file: str):
    print("reading", file)
    items_df = (pd.read_excel(file)
                  .reset_index(drop=True))
    return items_df
#

def empty_page():
    all_items = read_file('../../data/silent.xlsx')
    canv = canvas.Canvas(f"../../data/blank_silent.pdf", pagesize=A4)
    empty_item = AuctionItem(item_no='',
                             description='',
                             value='',
                             minimum_bid='',
                             increment='',
                             donor='',
                             title='',
                           )
    print(empty_item)
    front_page(empty_item, canv)
    produce_item_page(empty_item, canv)

    canv.showPage()
    canv.save()

if __name__ == '__main__':
    all_items = read_file('../../data/silent5.xlsx')
    canv = canvas.Canvas(f"../../data/silent.pdf", pagesize=A4)
    for index, item_row in all_items.iterrows():
        used_item = AuctionItem(item_no=item_row['Item#'],
                                description=item_row['Description'],
                                value=item_row['Retail Value'],
                                minimum_bid=item_row['Minimum Bid'],
                                increment=item_row['Minimum Bid Increment'],
                                donor=item_row['Donated By'],
                                title=item_row['Title'],
                                )
        print(used_item)
        front_page(used_item, canv)
        produce_item_page(used_item, canv)

        canv.showPage()
    canv.save()

    empty_page()
