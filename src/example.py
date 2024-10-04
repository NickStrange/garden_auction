from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib import colors
from reportlab.lib .styles import ParagraphStyle
import csv


def gen_body_table(width, height):
    widthList = [width*0.1, width*0.8, width*0.1]
    heightList = [height * 0.1, height * 0.15, height * 0.35, height*0.3, height * 0.1]

    leftPadding = 20
    tablesWidth = widthList[1] - leftPadding

    res = Table([
        ['', 'Offer', ''],
        ['', _genContactsTable(tablesWidth, heightList[1]), ''],
        ['', _genPriceListTable(tablesWidth, heightList[2]), ''],
        ['', _genDescriptionParas(), ''],
        ['', _genAboutTable(widthList[1], heightList[-1]), ''],
    ], colWidths=widthList,
       rowHeights=heightList
    )

    color = colors.HexColor('#003363')

    res.setStyle([
     #   ('GRID', (0, 0), (-1, -1), 1, 'red'),

        ('LINEBELOW', (1, 0), (1, 1), 1, color),
        ('LINEBELOW', (1, 3), (1, 3), 1, color),

        ('LEFTPADDING', (1, 0), (1, 3), leftPadding),

        ('FONTSIZE', (1,0), (1,0), 30),
        ('BOTTOMPADDING', (1, 0), (1, 0), 30),

        ('BOTTOMPADDING', (1, 1), (1, 2), 0),
        ('BOTTOMPADDING', (1, 3), (1, 3), 40),

        ('BOTTOMPADDING', (1, 4), (1, 4), 0),
        ('LEFTPADDING', (1, 4), (1, 4), 0),
    ]
    )

    return res

def _genContactsTable(width, height):
    widthList = [width*0.3, width*0.3,width*0.2, width*0.2]
    heightList = [height * 0.25] * 4

    matrix = []
    datalist = []
    with open(r'..\resources\tabledata.txt', 'r') as file:
        for line in file:
            if line != '\n':
                datalist.append(line.replace('\n',''))
    while len(datalist) % 4 != 0:
        datalist.append('')

    for row in range(4):
        line = ['', '', '', '']
        line[0] = datalist[row*4+0]
        line[1] = datalist[row*4 + 1]
        line[2] = datalist[row*4 + 2]
        line[3] = datalist[row*4 + 3]
        matrix.append(line)

    res = Table(matrix, colWidths=widthList, rowHeights=heightList)
    res.setStyle([
    #    ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('ALIGN', (3, 0), (3, -1), 'RIGHT'),
        ('RIGHTPADDING', (3, 0), (3, -1), 20),

        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ])
    return res

def _genPricesTable(width, height):
    matrix = []
    with open(r'..\resources\pricesTable.csv', 'r') as file:
        matrix = list(csv.reader(file))

    if len(matrix) < 2 or len(matrix[0]) != 6:
        return Table([['NO DATA']])

    widthList = [width*0.2, width * 0.2, width*0.25,
                 width * 0.15, width*0.1, width * 0.1]
    rowCount = len(matrix)
    color = colors.toColor('rgba(0, 115, 153, 0.9)')

    res = Table(matrix, colWidths=widthList, rowHeights=height/rowCount)
    res.setStyle([
        #  ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, 'grey'),
        ('BACKGROUND', (0, 0), (-1, 0), color),
        ('TEXTCOLOR', (0, 0), (-1, 0),'white'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (1, 1), (2, -1), 'CENTER'),
        ('ALIGN', (5, 1), (5, -1), 'RIGHT'),
        ('VALIGN', (1, 1), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.antiquewhite, colors.beige]),
    ])

    # for i in range(1, rowCount):
    #     if i%2 == 0:
    #         bc = colors.antiquewhite
    #     else:
    #         bc = colors.beige
    #     res.setStyle([('BACKGROUND', (0, i), (-1, i), bc)])

    return res

def _genPriceListTable(width, height):
    style = ParagraphStyle('titleprices')
    style.fontSize = 20
    style.fontName = 'Helvetica-Bold'
    style.spaceAfter = 15

    titlePara = Paragraph('DETAILS', style)
    pricesTable = _genPricesTable(width, height*0.7)

    elementsList = [titlePara, pricesTable]

    res = Table([
        [elementsList]
    ], colWidths=width, rowHeights=height)

    res.setStyle([
      #  ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('BOTTOMPADDING', (0, 0), (1, 0), 0),
    ])
    return res

def _genDescriptionParas():
    paraList = []

    para1Style = ParagraphStyle('para1d')
    para1Style.fontSize = 10
    para1Style.spaceAfter = 15
    para1Style.textColor = colors.HexColor('#003363')
    para1 = Paragraph("""
    <b>
    Thank you very much for using the services from us at Palms.
    Here at Palms Hotel we have living rooms and well-equipped
    meeting rooms of all sizes with a capacity from 8 - 300 people,
    so that we will be well prepared for most needs you may have.   
    </b>
    """, para1Style)

    para2Style = ParagraphStyle('para2d')
    para2Style.fontSize = 10
    para2 = Paragraph("""
    <i>
    Palms Hotel is also known for its cuisine and good service,
    therefore you can feel confident that your needs and desires
    will be well taken care of, whether you choose to use our
    beautiful Restaurant Palms or other living rooms,
    we guarantee a <u>good experience with us.</u>
    </i>
    """, para2Style)

    paraList.append(para1)
    paraList.append(para2)

    return paraList


def _genAboutTable(width, height):
    widthList = [width*0.2, width*0.8]

    image_path = '../resources/logoParadise.png'
    img = Image(image_path, widthList[0], height, kind='proportional')

    para1Style = ParagraphStyle('para1')
    para1Style.fontSize = 14
    para1Style.spaceAfter = 15

    para2Style = ParagraphStyle('para2')
    para2Style.fontSize = 8

    para1 = Paragraph('Palms Hotel', para1Style)
    para2 = Paragraph("""
    Ever since 2004, Palms Hotel has received accommodation and
    dining guests. The hotel and the restaurants has been run
    and owned by the Dubai SGPS.
    """, para2Style)
    paraList = [para1, para2]

    res = Table([
        [img, paraList],
    ], colWidths=widthList,
        rowHeights=height
    )

    res.setStyle([
     #   ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('BOTTOMPADDING', (0, 0), (1, 0), 0),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('VALIGN', (0, 0), (1, 0), 'MIDDLE'),
        ])
    return res