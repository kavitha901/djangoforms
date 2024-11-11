from django import forms
c=[('PYTHON','python'),['DJANGO','django'],('sql','sql')]
s=[['MALE','male'],['FEMALE','female']]
class StudentForms(forms.Form):
    Sname=forms.CharField()
    sid=forms.IntegerField()
    semail=forms.EmailField()
    surl=forms.URLField()
    spassword=forms.CharField(widget=forms.PasswordInput)
    saddress=forms.CharField(widget=forms.Textarea(attrs={'rows':10,'cols':10}))
    sgender=forms.ChoiceField(choices=s,widget=forms.RadioSelect)
    scourse=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    