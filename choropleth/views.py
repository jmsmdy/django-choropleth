from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PIL import Image
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import os
from io import BytesIO

def state(request, state):
    template = loader.get_template('choropleth/select_animal.html')
    animals = ['CATTLE, INCL CALVES',
               'CATTLE, COWS',
               'CATTLE, COWS, BEEF',
               'CATTLE, COWS, MILK',
               'CATTLE, (EXCL COWS)',
               'CATTLE, ON FEED',
               'HOGS',
               'SHEEP, INCL LAMBS',
               'GOATS',
               'GOATS, MILK',
               'GOATS, ANGORA',
               'GOATS, MEAT & OTHER',
               'EQUINE, HORSES & PONIES',
               'EQUINE, MULES & BURROS & DONKEYS',
               'CHICKENS, LAYERS',
               'CHICKENS, PULLETS, REPLACEMENT',
               'CHICKENS, BROILERS',
               'TURKEYS',
               'CHUKARS',
               'DUCKS',
               'EMUS',
               'GEESE',
               'GUINEAS',
               'PARTRIDGES, HUNGARIAN',
               'OSTRICHES',
               'PEAFOWL, HENS & COCKS',
               'PHEASANTS',
               'PIGEONS & SQUAB',
               'QUAIL',
               'RHEAS',
               'CHICKENS, ROOSTERS',
               'POULTRY, OTHER',
               'HONEY, BEE COLONIES',
               'ALPACAS',
               'BISON',
               'DEER',
               'ELK',
               'LLAMAS',
               'RABBITS, LIVE']
    context = {
        'state' : state,
        'animals' : animals
    }
    return HttpResponse(template.render(context, request))


def choropleth(request, state, animal):
    basedir = '/home/james/Django/project001/mapping/choropleth/data'
    fig, ax = plt.subplots(figsize=(10,10))
    US = gpd.read_file(os.path.join(basedir, 'UScounties.shp'))
    state_data = pd.read_csv(os.path.join(basedir, 'inventories', state, f'{animal}.csv'), dtype={'FIPS': str})
    data = US.merge(state_data, on='FIPS', how='right')
    data.plot('VALUE', cmap='OrRd',
                   ax=ax, legend=True,
                   legend_kwds={'label': f'INVENTORY OF {animal}',
                                'orientation': 'horizontal'})

    ax.axis("off")
    #canvas = FigureCanvasAgg(fig)
    buf = BytesIO()
    fig.savefig(buf, format='svg')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/svg+xml')
    #fig.savefig('temp.png')
    #im = Image.open('temp.png')
    #response = HttpResponse(content_type="image/png")
    #im.save(response, "PNG")
    return response

def detail(request):
    #print(request.POST)
    state = request.POST['state']
    animal = request.POST['animal']
    #state = 'MN'
    #animal = 'CATTLE, INCL CALVES'
    return HttpResponse(f'''
        <button onclick="goBack()">Go Back</button>
        <script>
        function goBack() {{
            window.history.back();
	}}
        </script>
	<h1> INVENTORY OF {animal} IN {state} </h1>
        <img src="{state}/{animal}">
	''')
