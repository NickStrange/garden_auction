from reportlab.platypus import Table, Image

def gen_header_table(width, height):

    width_list = [width * 0.2, width*0.6, width*0.2]

    left_image_path = '../data/roser.jpg'
    left_image_width = width_list[0]
    left_img = Image(left_image_path, left_image_width, height, kind='proportional')

    right_image_path = '../data/rosel.jpg'
    right_image_width = width_list[2]
    right_img = Image(right_image_path, right_image_width, height, kind='proportional')

    res = Table([
        [left_img, 'middle', right_img]], width_list, height)

    res.setStyle([       ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
    ])

    return res