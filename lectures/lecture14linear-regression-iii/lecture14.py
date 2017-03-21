import csv
import sys
sys.path.append('/vagrant/data-science-from-scratch/code/')  
import working_with_data as wwd

def load_ad_data():
    with open('Advertising.csv') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        parsers = {'Row': int, 'TV': float, 'Radio': float, 'Newspaper': float, 'Sales': float}
        data = [wwd.parse_dict(row, parsers) for row in data]
    return data
