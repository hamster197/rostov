from datetime import datetime
from django.shortcuts import render
from pycbrf.toolbox import ExchangeRates
from baks.forms import UsdImputForm


def dollars(request):
    if request.POST:
        form = UsdImputForm(request.POST)
        if form.is_valid():
            rates = ExchangeRates(datetime.now())['USD'].value
            if rates:
                result = str(rates * form.cleaned_data['usd_value'])+' рублей.'
            else:
                result = 'Сервис временно недоступен'
            return render(request, 'rate/post.html', {'tform': form, 'tresult':result})
    else:
        form = UsdImputForm()
    return render(request,'rate/post.html',{'tform':form})