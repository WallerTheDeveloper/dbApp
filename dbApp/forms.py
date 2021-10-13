from django.forms import ModelForm
from .models import Teachers, Students

class StudentForm(ModelForm):

   #Metadata
   class Meta :
       model = Students
       fields = ['name', 'surname', 'card_id', 'student_image']

class Teacherform(ModelForm):

   #Metadata
   class Meta :
       model = Teachers
       fields = '__all__'
