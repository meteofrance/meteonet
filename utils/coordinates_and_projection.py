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

#projection system
n_epsg = '4326'   #projection system used on the data -> EPSG:4326