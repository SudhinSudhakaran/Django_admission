from django.shortcuts import render
from faculties.models import faculty, student, student_leave
from faculties import views, urls

# Create your views here.
#students profile
def student_profile_view(request):
    slogin = student.objects.all().filter( semail = request.session['stud'] )
    #request.session['batch'] = querySet.fbatch
    return render(request,'student-profile.html',{'sdata':slogin})

#student profile edit view
def student_profile_edit(request):
    slogin = student.objects.all().filter( semail = request.session['stud'] )
    #request.session['batch'] = querySet.fbatch
    return render(request,'student_profile_edit.html',{'sdata':slogin})

#student profile update
def student_profile_update(request):
    ab = request.GET.get('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        qualification = request.POST.get('qualification')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        batch = request.POST.get('batch')
        dob = request.POST.get('dob')
        adddate = request.POST.get('adddate')
        blood = request.POST.get('blood')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password = request.POST.get('password')
        student.objects.filter(sadd_no = ab).update(sname=name, srollno=rollno, squalification=qualification, semail=email, sgender=gender,  fbatch=batch, sdob=dob, sadd_date=adddate, sblood=blood, smobile=mobile,  saddress=address, spassword=password )
        return render(request,'student_home.html')

#student new leave
def student_new_leave(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        batch = request.POST.get('batch')
        ltype = request.POST.get('ltype')
        lfrom = request.POST.get('leavefrom')
        lto = request.POST.get('leaveto')
        reason = request.POST.get('reason')
        a = student_leave(fbatch=batch, sname=name, srollno=rollno, sleave_from=lfrom, sleave_to=lto, sleave_type=ltype,  sleave_reason=reason)
        a.save()
        return render(request,'student_leave_management.html')

#student leave table
def student_leave_table(request):
    studentsview = student_leave.objects.all()#.filter( fbatch = request.session['batch'] )
    return render (request,'student-applied-leave.html',{'students':studentsview} )