from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from paragraph1 import gen_header_table
from src.auction_item import AuctionItem
from src.bid import set_bid_info
from src.description import set_description
from src.table import set_table
from src.title import set_title

def front_page(item: AuctionItem):
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
        ''
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

def back_page(item: AuctionItem):
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

pdf = canvas.Canvas("../data/auction.pdf", pagesize=A4)
pdf.setTitle("Palms Hotel")
item = AuctionItem(item_no=45,
                   description='Lovely sculpture to enhance the beauty of your garden',
                   value=80,
                   minimum_bid=40, #50%
                   increment=5,
                   donor="B J Huggins",
                   title="Garden Spinner")

front_page(item)
pdf.showPage()
back_page(item)
pdf.showPage()
pdf.save()