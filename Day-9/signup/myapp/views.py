from django.shortcuts import render

def homepageview(request):
    return render(request,'home.html')

def process(request):
    print(request.POST)
    a = (request.POST['name'])
    b = (request.POST['surname'])
    c = (request.POST['company'])
    d = (request.POST['email'])
    e = (request.POST['birthday'])
    f = (request.POST['designation'])
    g = (request.POST['branch'])
    h = (request.POST['salary'])
    i = (request.POST['mob_no.'])
    j = (request.POST['company_id'])
    return render(request,'feedback.html',{'mya':a ,'myb':b,'myc':c,'mye':e,'myf':f,'myg':g,'myh':h,'myi':i,'myj':j})