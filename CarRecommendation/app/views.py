from django.shortcuts import render
from django.db.models import Q
from .models import Car

import openai
import re



# Create your views here.

def get_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a car recommender"},
            {"role": "user", "content": message},  
        ]
    )
    answer = response.choices[0].message.content.strip()
    print(answer)
    return answer


def index(request):
    return render(request,"base.html")


def results(request):

    if request.method == 'POST':
        engine = request.POST.get('engine')
        fuel_type = request.POST.get('fuel_type')
        seats = request.POST.get('seats')
        price = request.POST.get('price')
        company = request.POST.get('company')
        features = request.POST.getlist('features')
        features_str = ''
        for i in range(0,len(features)):
            if( i == len(features)-1):
                features_str += features[i] + '.'
            else:
                features_str += features[i] + ','
        if company == 'Tata':
            message = "Suggest Tata cars of fuel_type " + fuel_type + "engine of " + engine + "having" + seats + "seats " + "and features such as " + features_str + 'within price range of' + price 
        else:
            message = "Suggest Non Tata cars in India of fuel_type " + fuel_type + "engine of " + engine + "having" + seats + "seats " + "and features such as " + features_str + 'within price range of' + price

        response = get_response(message)
        split = re.split(r'\. |\n|, |: | ', response)
        print(split)

        filter_query = Q()
        for name in split:
            filter_query |= Q(name=name)

        filtered_products = Car.objects.filter(filter_query)
        context = {
            'response' : response,
            'filtered_products' : filtered_products
        }

        return render(request,'results.html',context)
