from reportlab.lib import colors
from reportlab.platypus import Table

from src.garden.auction_item import AuctionItem


def set_table(width: int, height: int, item: AuctionItem):
    width_list = [width*0.075, width * 0.15, width*0.35, width * 0.125]
    color = colors.toColor('rgba(0, 115, 153, 0.9)')
    matrix = [['', 'BIDDER PHONE', 'BIDDER NAME', 'BID AMOUNT']]
    linecount = 16
    if item.minimum_bid != '':
        min = int(item.minimum_bid)
    else:
        min = ''
    matrix += [['1', '', '', f'${min}']]
    offset = 2
    for i in range(linecount-2):
        matrix += ([[i+offset, '', '', '']])
    res = Table(matrix, colWidths=width_list, rowHeights=height/linecount)
    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, 'grey'),
        ('BACKGROUND', (0, 0), (-1, 0), color),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (1, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1),  [colors.white, colors.lightgrey]),
    ])

    return res
