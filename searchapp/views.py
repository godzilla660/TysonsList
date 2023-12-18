from requests.compat import quote_plus
import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

from . import models

# Create your views here.

BASE_CRAIGSLIST_URL = 'https://kenya.craigslist.org/search/sss?query={}'


def home(request):
    return render(request, 'base.html')


def newsearch(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_listings = soup.find_all('li', {'class': 'span.label'})
    print(post_listings)

    # post_title = post_listings[0].find(class_='result-title').text
    # post_url = post_listings[0].find('a').get('href')
    # post_price = post_listings[0].find(class_='result-price').text
    #
    # print(post_title)
    # print(post_url)
    # print(post_price)

    context = {
        'search': search
    }
    return render(request, 'searchapp/new_search.html', context)
