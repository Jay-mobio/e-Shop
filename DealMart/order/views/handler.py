from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse,render
from order.paytm import Checksum
from order.views.order import MERCHANT_KEY

@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPONSE'] == '01':
            print("Order successful")
        else:
            print('order was not successful because' + response_dict["RESPMSG"])
    return render(request,'order/paymentsuccessful.html',{'response':response_dict})