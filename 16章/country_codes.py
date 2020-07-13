'''提取国家国际简码'''

from  pygal_maps_world.i18n import COUNTRIES

def get_w_j(country_name):
    for code , name in  COUNTRIES.items():
        if name == country_name:
            return code

    return None
