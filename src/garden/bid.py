from reportlab.platypus import Table


def set_bid_info(width: int, height: int, minimum_bid: float, increment: float):
    height_list = [0.5*height, 0.5*height]

    bid_table = Table([
        [f'MINIMUM BID ${minimum_bid}'],
        [f'MINIMUM BID INCREMENT: ${increment}'],
    ], colWidths=width,
       rowHeights=height_list)

    bid_table.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        # # minimum bid
        ('ALIGN', (0, 0), (0, 0), 'CENTRE'),
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (0, 0), 10),
        ('FONTSIZE', (0, 0), (0, 0), 10),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        # # # minimum bid
        ('ALIGN', (0, 1), (0, 1), 'CENTRE'),
        ('VALIGN', (0, 1), (0, 1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (0, 1), 10),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica-Bold'),
    ])

    return bid_table
