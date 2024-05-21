from django.shortcuts import render
#from django.http import HttpResponse
#from django.views.generic import TemplateView
#from .forms import SessionForm
from .models import Friend
from .forms import HelloForm

"""
class HelloView(TemplateView):

    def __init__(self):
        self.params={
            'title':'Hello',
            'form':SessionForm(),
            'result':None
        }

    def get(self,request):
        self.params['result'] = request.session.get('last_msg','No messsage.')
        return render(request, 'hello/index.html', self.params)
        
    def post(self,request):
        ses=request.POST['session']
        self.params['result'] ='send: "' + ses + '".' 
        request.session['last_msg']=ses
        self.params['form']=SessionForm(request.POST)
        return render(request,'hello/index.html', self.params)

def sample_middleware(get_response):

    def middleware(request):
        counter = request.session.get('counter',0)
        request.session['counter']=counter+1
        response=get_response(request)
        print("count: " +str(counter))
        return response
    
    return middleware
"""
def index(request):
    params={
        'title':'Hello',
        'message':'all friend.',
        'form':HelloForm(),
        'data':[],
    }
    if (request.method =='POST'):
        num=request.POST['id']
        item = Friend.objects.get(id=num)
        params['data']=[item]
        params['form']=HelloForm(request.POST)
    else:
        params['data']=Friend.objects.all()
    return render(request,'hello/index.html',params)
# Create your views here.
