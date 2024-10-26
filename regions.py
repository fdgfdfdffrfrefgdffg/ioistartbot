import json

def get_districts(selected_region_id):
    with open('districts.json', 'r', encoding='cp1251') as f:
        districts = json.load(f)
    with open('regions.json', 'r', encoding='cp1251') as f:
        regions = json.load(f)

    filtered_districts = [d for d in districts if d['region_id'] == selected_region_id]
    if filtered_districts:
        return filtered_districts

def get_regions():
    with open('regions.json', 'r', encoding='cp1251') as f:
        regions = json.load(f)
    return regions

def get_region(region_id):
    with open('regions.json', 'r', encoding='cp1251') as f:
        regions = json.load(f)
    for region in regions:
        if region["id"] == region_id:
            return region
        
def get_district(district_id):
    with open('districts.json', 'r', encoding='cp1251') as f:
        districts = json.load(f)
    for district in districts:
        if district["id"] == district_id:
            return district