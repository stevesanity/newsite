from django.shortcuts import *
from showdata.form import *
from showdata.models import *
from datetime import datetime
from django.http import *


# Create your views here.
# test part
def show_data(request):
    med_data = MedicationData.objects.all()
    data = []
    for row in med_data:
        data.append([row.ID,row.DateTime,row.SEX,row.AntRvWall])
        #print(row.DateTime)
        
    return render_to_response('showdata.html',{'data':data})


def add_data(request,new_id):
    time = datetime.now()
    med_data = MedicationData(int(new_id),
                              time,
                              'woman',
                              1,
                              1.00,
                              0,
                              1.000,
                              1.00,
                              1.00,
                              1.00,
                              1,
                              'str',
                              1.00,
                              0,
                              0,
                              0,
                              1.000,
                              1.00,
                              0,
                              1.000,
                              0,
                              0,
                              0,
                              1.000,
                              0,
                              1.000,
                              0,
                              0,
                              9,
                              'ch',
                              'char',
                              0,
                              0,
                              1.00000,
                              1.000,
                              1.000,
                              0,
                              0,)
    med_data.save()
    return render_to_response('add_data.html',{'id':new_id,'time':time})

# normal part
def front_page(request):
    return render_to_response('frontpage.html')


def main_dashboard(request):
    return render_to_response('maindashboard.html')


# account creating
def account_edit(request):
    if request.method == 'POST':
        form = Accounteditform(request.POST)
        if form.is_valid() and request.POST['Pass_word'] == request.POST['Pass_word_reaffirm']:
            accountdata = Account (
                FirstName = request.POST['First_name'],
                LastName = request.POST['Last_name'],
                EmailAddress = request.POST['Email_address'],
                PassWord = request.POST['Pass_word']
            )
            accountdata.save()
            return HttpResponseRedirect('maindashboard.html')
    return render_to_response('account.html')

# log in verifying
def log_in_verifying(request):
    if request.method == 'POST':
        form = Loginverifyingform(request.POST)
        if form.is_valid() and request.POST['Pass_word'] == Account.objects.get(EmailAddress=request.POST['Email_address']).PassWord:
            return HttpResponseRedirect('maindashboard.html')
    return render_to_response('login.html')



def intro_risk_prediction(request):
    return render_to_response('introriskpredicton.html')

def intro_health_alert(request):
    return render_to_response('introhealthalert.html')

def test_index(request):
    return render_to_response('testindex.html')

def test_smart(request):
    return render_to_response('testsmart.html')

