import json, os

base_dir = os.path.dirname(os.path.abspath(__file__))
district_path = os.path.join(base_dir, 'districts.json')
regions_path = os.path.join(base_dir, 'regions.json')
def get_districts(selected_region_id):
    with open(district_path, 'r', encoding='cp1251') as f:
        districts = json.load(f)
    with open(regions_path, 'r', encoding='cp1251') as f:
        regions = json.load(f)

    filtered_districts = [d for d in districts if d['region_id'] == selected_region_id]
    if filtered_districts:
        return filtered_districts

def get_regions():
    with open(regions_path, 'r', encoding='cp1251') as f:
        regions = json.load(f)
    return regions

def get_region(region_id):
    with open(regions_path, 'r', encoding='cp1251') as f:
        regions = json.load(f)
    for region in regions:
        if region["id"] == region_id:
            return region
        
def get_district(district_id):
    with open(district_path, 'r', encoding='cp1251') as f:
        districts = json.load(f)
    for district in districts:
        if district["id"] == district_id:
            return district