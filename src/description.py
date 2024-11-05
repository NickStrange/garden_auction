from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, Image, Paragraph

from src.auction_item import AuctionItem


def setdesc(width, height, item:AuctionItem):
    colwidth=[0.05*width, 0.90*width, 0.0*width]
    para1Style = ParagraphStyle('para1d')
    para1Style.fontSize = 15
    para1Style.spaceAfter = 5
    para1Style.textColor = colors.HexColor('#003363')
    para1 = Paragraph(item.description, para1Style)
    para2Style = ParagraphStyle('para2d')
    para2Style.fontSize = 15
    para2Style.spaceAfter = 5
    para2Style.textColor = colors.HexColor('#003363')
    para2 = Paragraph(f' Donated by: {item.donor}', para2Style)
    descTable = Table([
        ['', para1, ''],
        ['', para2, '']
    ], colWidths=colwidth,
       rowHeights=[height*10/16, height*3/16])
    # description section
    descTable.setStyle([
 #   ('GRID', (0, 0), (-1, -1), 1, 'blue'),
    ('GRID', (1, 0), (1, 1), 1, 'black'),
    ('BOTTOMPADDING', (0, 0), (0, 0), 0),
    ('BOTTOMPADDING', (1, 0), (1, 0), 0),
    ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
    ('VALIGN', (0, 0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1,-1), 5),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold')])

    return descTable

def set_description(width:int, height:int,item: AuctionItem):
    heightList = [5, 100, 10, 20]
    heightList = [height*0.1, height*0.6, height*0.1, height*0.2]
    buy_now = '** THIS IS A BUY NOW ITEM **' if item.buy_now else ''
    descriptionTable = Table([
        [f'ITEM #{item.item_no} {item.title}'],
        [setdesc(width, heightList[1]-5, item)],
        [f'RETAIL VALUE: ${item.value} {buy_now}'],
        [f'MINIMUM BID ${item.minimum_bid}. MINIMUM BID INCREMENT: ${item.increment}'],
    ], colWidths=width,
       rowHeights=heightList)

    descriptionTable.setStyle([
      #  ('GRID', (0, 0), (-1, -1), 1, 'green'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        # # top section
        ('ALIGN', (0,0), (0,0), 'CENTRE'),
        ('VALIGN', (0,0), (0,0), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (0, 0), 20),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),

        # retail price section
        ('ALIGN', (0, 2), (0, -1), 'CENTRE'),
        ('VALIGN', (0, 2), (0, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 2), (0, -1), 0),
        ('FONTSIZE', (0, 2), (0, -1), 20),
        ('FONTNAME', (0, 2), (0, -1), 'Helvetica-Bold'),
    ])

    return descriptionTable