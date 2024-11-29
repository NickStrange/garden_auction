from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, Image, Paragraph

from src.auction_item import AuctionItem


def setdesc(width, height, item:AuctionItem):
    colwidth=[0.05*width, 0.90*width, 0.0*width]
    para2Style = ParagraphStyle('para2d')
    para2Style.fontSize = 15
    para2Style.spaceAfter = 5
    para2Style.textColor = colors.HexColor('#003363')
    para2 = Paragraph(f' Donated by: ')
    descTable = Table([
        ['', '', ''],
        ['', para2, '']
    ], colWidths=colwidth,
       rowHeights=[height*13/16, height*3/16])
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
    heightList = [height*0.05, height*0.75, height*0.15, height*0.05]
    descriptionTable = Table([
        [''],
        [setdesc(width, heightList[1], item)],
        [f'RETAIL VALUE: '],
        [''],
    ], colWidths=width,
       rowHeights=heightList)

    descriptionTable.setStyle([
    #    ('GRID', (0, 0), (-1, -1), 1, 'green'),
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