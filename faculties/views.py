from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from faculties.models import faculty, student
from students import urls

# Create your views here.


#login
def login(request):
    if request.method=='POST':
        email= request.POST.get('email')
        password = request.POST.get('password')
        email=str(email)
        password=str(password)
        u=faculty.objects.filter(fpassword = password)
        p=faculty.objects.filter(femail = email)
        if (u.count()==1 and p.count()==1):
            request.session['fac']=email
            #QuerySet = faculty.objects.all().filter( femail = email )
            return render(request,'faculty-home.html')
        else:
            c = student.objects.filter(spassword = password)
            d = student.objects.filter(semail = email)
            if c.count()==1 and d.count()==1:
                request.session['stud']=email
                QuerySet = student.objects.all().filter( semail = email )
                return render(request,'student_home.html',{'data':QuerySet})
            else:
                return HttpResponse("login unsuccessfull")


#admin logout
def flogout(request):
    logout(request)
    return render(request,'index.html')

#faculty profile
def faculty_profile(request):
    querySet = faculty.objects.all().filter( femail = request.session['fac'] )
    request.session['batch'] = querySet.fbatch
    return render(request,'faculty_profile.html',{'fdata':querySet})

#faculty profile edit
def faculty_profile_edit(request):
    querySet = faculty.objects.all().filter( femail = request.session['fac'] )
    return render(request,'faculty_profile_edit.html',{'fdata':querySet})

#faculty profile update
def faculty_profile_update(request):
    ab = request.GET.get('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        joindate = request.POST.get('joindate')
        qualification = request.POST.get('qualification')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        batch = request.POST.get('batch')
        blood = request.POST.get('blood')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        password = request.POST.get('password')
        faculty.objects.filter(fid = ab).update(fname=name, fdesignation=designation, fjoin_date=joindate, fqualification=qualification, fgender=gender, fmobile=mobile, femail=email, fbatch=batch, fblood=blood, fdob=dob, faddress=address, fpassword=password )
        return render(request,'faculty-home.html')


#faculty student table
def faculty_student_table(request):
    #batch = request.GET.get('batch')
    studentsview = student.objects.all()#.filter( fbatch = request.session['batch'] )
    return render (request,'faculity_home_batch.html',{'students':studentsview} )


#faculty student profile view
def studentprofile(request):
    ba = request.GET.get('mail')
    studentview = student.objects.get().filter(semail=ba)
    return render (request,'faculty_student_details.html',{'sview':studentview})

#faculty profile update
def faculty_new_student(request):
    if request.method == 'POST':
        addno = request.POST.get('Addno')
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        qualification = request.POST.get('qualification')
        email = request.POST.get('mail')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        batch = request.POST.get('batch')
        dob = request.POST.get('dob')
        blood = request.POST.get('blood')
        adddate = request.POST.get('adddate')
        address = request.POST.get('address')
        password = request.POST.get('password')
        a = student(sadd_no=addno, sname=name, srollno=rollno, squalification=qualification, sgender=gender, fbatch=batch, sdob=dob, sadd_date=adddate, sblood=blood, smobile=mobile, semail=email, saddress=address, spassword=password )
        a.save()
        return render(request,'faculity_home_batch.html')