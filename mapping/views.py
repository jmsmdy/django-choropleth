from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('select.html')
    return HttpResponse(template.render({}, request))

def index_old(request):
    template = loader.get_template('select.html')
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
    states = ['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'FM', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MH', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'PW', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY']
    context = {
        'states' : states,
        'animals' : animals
    }
    return HttpResponse(template.render(context, request))
