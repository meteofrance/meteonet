import json

#coordinates of boundaries of study zones
def create_dic_borne(N,S,W,E):
    dic = {
        'uly' : N,
        'lry' : S,
        'ulx' : W,
        'lrx' : E
    }
    return dic

DOMAINS = {
    'NW'   :  create_dic_borne( 51.896, 46.25, -5.842, 2),
    'SE'  :  create_dic_borne( 46.25, 41.1, 2, 9.842)
    }


#color palette about CT (Cloud Type) satellite data

CLOUD_TYPE_16 = {
    "0":"No data",
    "1":"Cloud-free land",
    "2":"Cloud-free sea",
    "3":"Snow over land",
    "4": "Sea ice",
    "5":"Very low clouds",
    "6":"Low clouds",
    "7":"Mid-level clouds",
    "8":"High opaque clouds",
    "9":"Very high opaque clouds",
    "10":"Fractional clouds",
    "11":"High semi transparent thin clouds",
    "12":"High semi transparent meanly thick clouds",
    "13":"High semi transparent thick clouds",
    "14":"High semi transparent above low or medium clouds",
    "15":"High semi transparent above snow/ice"
}

CT_16_COLOR_MAP = [[0.39215686, 0.39215686, 0.39215686],
                   [0., 0.47058824, 0.],
                   [0., 0., 0.],
                   [0.98039216, 0.74509804, 0.98039216],
                   [0.8627451, 0.62745098, 0.8627451],
                   [1., 0.39215686, 0.],
                   [1., 0.70588235, 0.],
                   [0.94117647, 0.94117647, 0.],
                   [0.84313725, 0.84313725, 0.58823529],
                   [0.90196078, 0.90196078, 0.90196078],
                   [0.78431373, 0., 0.78431373],
                   [0., 0.31372549, 0.84313725],
                   [0., 0.70588235, 0.90196078],
                   [0., 0.94117647, 0.94117647],
                   [0.35294118, 0.78431373, 0.62745098],
                   [1, 0.6, 1]]

#color palette about VIS06 channel satellite data
def vis_palette(palette_name):
    m = []
    M = []
    c = []
    with open('../../meteonet_toolbox/color_palettes/'+ palette_name) as f:
        color_data = json.load(f)
    for i in range(0,len(color_data['levels'])):
        m.append(color_data['levels'][i]['min'])
        M.append(color_data['levels'][i]['max'])
        c.append(color_data['levels'][i]['color'])
    m.append(M[len(M)-1])
    m.insert(0,-1)
    c.insert(0,'dodgerblue')
    return m,c

#color palette about IR channels satellite data
def ir_palette(palette_name):
    m = []
    M = []
    c = []
    with open('../../meteonet_toolbox/color_palettes/'+ palette_name) as f:
        color_data = json.load(f)
    for i in range(0,len(color_data['levels'])):
        m.append(color_data['levels'][i]['min'])
        M.append(color_data['levels'][i]['max'])
        c.append(color_data['levels'][i]['color'])
    m.insert(0,M[0])
    m.reverse()
    c.reverse()
    return m,c