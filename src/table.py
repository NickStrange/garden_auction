from reportlab.lib import colors
from reportlab.platypus import Table, Image

from src.auction_item import AuctionItem


def set_table(width:int, height:int, item:AuctionItem, front=True):
    widthList = [width*0.075, width * 0.15, width*0.35, width * 0.125]
    color = colors.toColor('rgba(0, 115, 153, 0.9)')
    matrix = [['', 'BIDDER #', 'BIDDER NAME', 'BID AMOUNT']]
    front_lines=16
    if front:
        linecount=front_lines
        matrix += [['1', '', '', f'${item.minimum_bid}']]
        offset = 2
    else:
        linecount=28
        offset = front_lines-1
        matrix += [[front_lines, '', '', '']]
    for i in range(linecount-2):
        matrix+=([[i+offset,'','', '']])
    res = Table(matrix, colWidths=widthList, rowHeights=height/linecount)
    res.setStyle([
       # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, 'grey'),
        ('BACKGROUND', (0, 0), (-1, 0), color),
        ('TEXTCOLOR', (0, 0), (-1, 0),'white'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (1, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.antiquewhite, colors.beige]),
    ])

    return res