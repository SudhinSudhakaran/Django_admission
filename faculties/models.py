from django.db import models

# Create your models here.
#faculty table
class faculty(models.Model):
    fid = models.CharField(max_length = 20, primary_key = True)
    fname = models.CharField(max_length = 100)
    fdesignation = models.CharField(max_length = 50)
    fjoin_date = models.DateField()
    fqualification = models.CharField(max_length = 10)
    fgender = models.CharField(max_length = 10)
    fmobile = models.IntegerField()
    femail = models.EmailField(max_length=100)
    fbatch = models.CharField(max_length = 10)
    fblood = models.CharField(max_length = 10)
    fdob = models.DateField()
    faddress = models.CharField(max_length = 200)
    fpassword = models.CharField(max_length = 50)

    class Meta:
        db_table = 'faculty'

#student table
class student(models.Model):
    sadd_no = models.CharField(max_length = 20, primary_key = True)
    sname = models.CharField(max_length = 100)
    srollno = models.IntegerField()
    squalification = models.CharField(max_length = 10)
    sgender = models.CharField(max_length = 10)
    fbatch = models.CharField(max_length = 10)
    sdob = models.DateField()
    sadd_date = models.DateField()
    sblood = models.CharField(max_length = 10)
    smobile = models.IntegerField()
    semail = models.EmailField(max_length=100)
    saddress = models.CharField(max_length = 200)
    spassword = models.CharField(max_length = 50)

    class Meta:
        db_table = 'student'

#students leave
class student_leave(models.Model):
    fbatch = models.CharField(max_length = 10)
    sname = models.CharField(max_length = 100)
    srollno = models.IntegerField()
    sleave_from = models.CharField(max_length = 50)
    sleave_to = models.CharField(max_length = 50)
    sleave_type = models.CharField(max_length = 100)
    sleave_reason = models.CharField(max_length = 500)
    sleave_status = models.CharField(max_length = 50, default='pending')

    class Meta:
        db_table = 'student-leave'