import numpy as np

#coordinates of boundaries of study zones
def create_dic_borne(N,S,W,E):
    dic = {
        'uly' : N,
        'lry' : S,
        'ulx' : W,
        'lrx' : E
    }
    return dic

def get_sat_coordinate(zone):
    """
    Return lat lon coordinate of satellite data 
    """
    lllat=DOMAINS[zone]['lry']    #lower left latitude
    urlat=DOMAINS[zone]['uly']    #upper right latitude
    lllon=DOMAINS[zone]['ulx']    #lower left longitude
    urlon=DOMAINS[zone]['lrx']    #upper right longitude
    d = {}
    d["lon"] = np.arange(lllon,urlon-0.0425/2,0.0425)
    d["lat"] = np.arange(urlat,lllat + 0.0425/2,-0.0425)
    return d

DOMAINS = {
    'NW'   :  create_dic_borne( 51.896, 46.25, -5.842, 2),
    'SE'  :  create_dic_borne( 46.25, 41.1, 2, 9.842)
    }

SAT_COORD = { 'NW': get_sat_coordinate("NW"),
              'SE': get_sat_coordinate("SE")
}

#projection system
n_epsg = '4326'   #projection system used on the data -> EPSG:4326

CLOUD_TYPE = {
    "0":"No data",
    "1":"Cloud-free land",
    "2":"Cloud-free sea",
    "3":"Snow over land",
    "4":"Sea ice",
    "5":"Very low clouds cum.",
    "6":"Very low clouds str.",
    "7":"Low cloud cum.",
    "8":"Low cloud str.",
    "9":"Mid-level coulds cum.",
    "10":"Mid-level clouds str.",
    "11":"High opaque clouds cum.",
    "12":"High opaque clouds str.",
    "13":"Very high opaque clouds cum.",
    "14":"Very high opaque clouds str.",
    "15":"High semi transparent thin clouds",
    "16":"High semi transparent meanly thick clouds",
    "17":"High semi transparent thick clouds",
    "18":"High semi transparent above low or medium clouds",
    "19":"Fractional clouds",
    "20":"No value",
}
CT_COLOR_MAP = [[0.39215686, 0.39215686, 0.39215686], [0., 0.47058824, 0.], [0., 0., 0.],
 [0.98039216, 0.74509804, 0.98039216], [0.8627451, 0.62745098, 0.8627451],
 [1., 0.58823529, 0.], [1., 0.39215686, 0.], [1., 0.8627451, 0.],
 [1., 0.70588235, 0.], [1., 1., 0.54901961], [0.94117647, 0.94117647, 0.],
 [0.98039216, 0.94117647, 0.78431373], [0.84313725, 0.84313725, 0.58823529],
 [1., 1., 1.], [0.90196078, 0.90196078, 0.90196078],
 [0., 0.31372549, 0.84313725], [0., 0.70588235, 0.90196078],
 [0., 0.94117647, 0.94117647], [0.35294118, 0.78431373, 0.62745098],
 [0.78431373, 0., 0.78431373], [0.37254902, 0.23529412, 0.11764706]]