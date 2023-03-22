#!/usr/bin/python3.11

# Scraping Bicycle Geometry info from geometrics.mtb-news.de

# bikes are nested in:
#
# div class=" container mtbnews-geometry-content__container"
#   --> div class="col"
#     --> div class="row" 
#       --> p class="mtbnews-geometry__bike-meta"
#         --> a href="https://geometrics.mtb-news.de/bike-category/XYZ/"

import requests
from bs4 import BeautifulSoup
import polars as pl

entry_url = 'https://geometrics.mtb-news.de/'
target_class_list = 'mtbnews-geometry__bike-list'

# Get the page
page = requests.get(entry_url)
soup = BeautifulSoup(page.content, 'html.parser')

# select the bike sublists (0-9, A-Z)
sublists = soup.find_all('ul', attrs={'class':target_class_list})

# the desired columns
columns = [
    'Model',
    'Category',
    'Frame Size',
    'Wheel Size',
    'Reach',
    'Stack',
    'STR',
    'Front-Center',
    'Head Tube Angle',
    'Seat Tube Angle Effective',
    'Seat Tube Angle Real',
    'Top Tube Length',
    'Top Tube Length Horizontal',
    'Steerer Tube Length',
    'Seat Tube Length',
    'Standover Height',
    'Chainstay Length',
    'Wheelbase',
    'Bottom Bracket Drop',
    'Bottom Bracket Height',
    'Fork Stack Height',
    'Fork Offset',
    'Fork Trail',
    'Suspension Travel (rear)',
    'Suspension Travel (front)',
]
# for empty dict
values = [[] for name in columns]

# create empty entry dict
data = dict(zip(columns, values))

# follow links to individual bikes (default tab on load lists all bike categories)
for i, ul in enumerate(sublists):
    # print(i)
    # if i == 2:
    #     break
    for li in ul.find_all('li'):
        # print('Getting Page: ')
        # print(li.find('a').get('href'))
        # follow href to individual bike page 
        bikeurl = li.find('a').get('href')
        bikepage = requests.get(bikeurl)
        bikesoup = BeautifulSoup(bikepage.content, 'html.parser')
        # get the category from page link
        category = bikesoup.find(
            'div', attrs={'class':'row'}
        ).find(
            'div', attrs={'class':'col'}
        ).find(
            'p', attrs={'class':'mtbnews-geometry__bike-meta'}
        ).find(
            'a'
        ).text

        print(f'URL:\t\t{bikeurl} \nCategory:\t{category}')
        # get the table
        table = []
        rows = []
        try:
            table = bikesoup.find('table')
            rows = table.find('tbody').find_all('tr')
        except:
            print('No table found')
            continue

        # if table contains select elements, skip this one as it will export incorrectly
        try:
            table.find_all('select').pop()
            print('Found select elements -> skipping this table')
            continue
        except:
            pass
        
        #print(f'Rows (const):\t{len(rows)}')
        print(f'Variants:\t{len(rows[0].find_all("td"))}\n')
        # extract values from table
        for row in rows:

            selectopt = None
            
            for idx, col in enumerate(row.find_all('td')):

                colval = col.text.strip(' \t\n\r')
                # match value to the current row header
                match row.find('th').text.strip(' \t\n\r'):
                    case 'Modell':
                        data['Model'].append(colval)
                    case 'Rahmengröße/Setup':
                        data['Frame Size'].append(colval)
                    case 'Typ':
                        data['Category'].append(colval)
                    case 'Laufradgröße':
                        data['Wheel Size'].append(colval)
                    case 'Reach':
                        data['Reach'].append(colval)
                    case 'Stack':
                        data['Stack'].append(colval)
                    case 'STR':
                        data['STR'].append(colval)
                    case 'Front-Center':
                        data['Front-Center'].append(colval)
                    case 'Lenkwinkel':
                        data['Head Tube Angle'].append(colval)
                    case 'Sitzwinkel, effektiv':
                        data['Seat Tube Angle Effective'].append(colval)
                    case 'Sitzwinkel, real':
                        data['Seat Tube Angle Real'].append(colval)
                    case 'Oberrohrlänge':
                        data['Top Tube Length'].append(colval)
                    case 'Oberrohrlänge (horizontal)':
                        data['Top Tube Length Horizontal'].append(colval)
                    case 'Steuerrohrlänge':
                        data['Steerer Tube Length'].append(colval)
                    case 'Sitzrohrlänge':
                        data['Seat Tube Length'].append(colval)
                    case 'Überstandshöhe':
                        data['Standover Height'].append(colval)
                    case 'Kettenstrebenlänge':
                        data['Chainstay Length'].append(colval)
                    case 'Radstand':
                        data['Wheelbase'].append(colval)
                    case 'Tretlagerabsenkung':  
                        data['Bottom Bracket Drop'].append(colval)
                    case 'Tretlagerhöhe':
                        data['Bottom Bracket Height'].append(colval)
                    case 'Einbauhöhe Gabel':
                        data['Fork Stack Height'].append(colval)  
                    case 'Gabel-Offset':
                        data['Fork Offset'].append(colval)
                    case 'Gabel-Nachlauf':
                        data['Fork Trail'].append(colval)
                    case 'Federweg (hinten)':  
                        data['Suspension Travel (rear)'].append(colval)
                    case 'Federweg (vorn)':   
                        data['Suspension Travel (front)'].append(colval)
                    case _:
                        # there is an empty row header, the row is used for compare buttons -> ignore
                        pass 
                        # errcase = row.find('th').text
                        # print(f'Unhandled case: {errcase}')



#print(data)
# for (key,val) in data:
#     print(f'{key}: {len(val)}')

# construct data frame from dict
df = pl.DataFrame(data)
print(df.head(), df.shape)
df.write_csv('resources/data/bicycles/geometrics.mtb-news.skip.csv', sep=';')
df.write_ipc('resources/data/bicycles/geometrics.mtb-news.skip.arrow', compression='zstd')

