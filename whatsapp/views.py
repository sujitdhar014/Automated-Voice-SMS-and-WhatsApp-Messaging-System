from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

@csrf_exempt
def index(request):
    return render(request, 'index.html')



@csrf_exempt
def send_message(request):
    if request.method == 'GET':
        phone_number = request.GET.get('phone_number', '')
        message_type = request.GET.get('message_type', '')
        message_body = request.GET.get('message_body', '')

        # Twilio API sid and token
        account_sid = 'AC4c027ee90a30c2ea074264d35c8768bc'
        auth_token = '5f400ab64d1cd7ecd7441e927ed82eac'
        client = Client(account_sid, auth_token)

        if message_type == 'whatsapp':
         
            message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to='whatsapp:+916003883840'
        )

            print(message.sid)

          ####voice call
        elif message_type == 'voice_call':
            call = client.calls.create(
                url='http://demo.twilio.com/docs/voice.xml',
                        to='+916003883840',
                        from_='+12058505943'
                    )

            print(call.sid)
            #sms 
        elif message_type == 'sms':
            message = client.messages.create(
            body=message_body,
            from_='+12058505943',
            to='+916003883840'        
        )

            print(message.sid)
            

        else:
            print("Try Again:")
           


@csrf_exempt
def messagecom(request):
    user = request.POST.get('From')
    message_content = request.POST.get('Body')
    return render(request, 'message_template.html', {'user': user, 'message': message_content})




@csrf_exempt
def message(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    print(f'{user} says {message}')


    response = MessagingResponse()
    response.message('Thank for your message! A member of our team will be '
                     'in touch with you soon.')
    return HttpResponse(str(response))


