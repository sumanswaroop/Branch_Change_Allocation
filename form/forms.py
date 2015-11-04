from django import forms
from form.models import userpost,program


class userpostform(forms.ModelForm):
	g='GE'
	o='OBC'
	s='SC'
	t='ST'
	CHOICELIST = ((g,g),(o,o),(s,s),(t,t),)


	a ='AE B.Tech'
	b='CE B.Tech'
	c='CH'
	d='CL B.Tech'
	e='CL Dual Deg'
	f='CS B.Tech'
	ge='EE B.Tech'
	h='EE Dual Deg E1'
	i='EE Dual Deg E2'
	j='EN Dual Deg'
	k='EP B.Tech'
	l='EP Dual Deg N1'
	m='ME B.Tech'
	n='ME Dual Deg M2'
	om='MM B.Tech'
	p='MM Dual Deg Y1'
	q='MM Dual Deg Y2'


	BRANCHLIST = (('' , 'None' ),(a,a),(b,b),(c,c),(d,d),(e,e),(f,f),(ge,ge),(h,h),(i,i),(j,j),(k,k),(l,l),(m,m),(n,n),(om,om),(p,p),(q,q),)

	Category = forms.ChoiceField(choices=CHOICELIST ,widget=forms.Select(attrs={'class':'form-control'}))
	Present_Branch = forms.ChoiceField(choices=BRANCHLIST ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_1 = forms.ChoiceField(choices=BRANCHLIST ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_2 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_3 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_4 = forms.ChoiceField(choices=BRANCHLIST , required = False,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_5 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_6 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_7 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_8 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_9 = forms.ChoiceField(choices=BRANCHLIST , required = False,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_10 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_11 = forms.ChoiceField(choices=BRANCHLIST , required = False,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_12 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_13 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_14 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_15 = forms.ChoiceField(choices=BRANCHLIST , required = False,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_16 = forms.ChoiceField(choices=BRANCHLIST, required = False ,widget=forms.Select(attrs={'class':'form-control'}))

	class Meta:
		model = userpost
		fields = ('rollno' ,'name' ,'Category' ,'Present_Branch', 'cpi' ,'Preference_1','Preference_2','Preference_3','Preference_4','Preference_5','Preference_6','Preference_7','Preference_8','Preference_9','Preference_10','Preference_11','Preference_12','Preference_13','Preference_14','Preference_15','Preference_16')
		widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name' , 'class': 'form-control' }),
            'rollno': forms.TextInput(attrs={'placeholder': '15XXXXXXX Roll' , 'class': 'form-control', 'readonly':'true' }),
            'cpi': forms.TextInput(attrs={'placeholder': 'CPI in [0:10]' , 'class': 'form-control' }),
            'pbranch': forms.TextInput(attrs={'placeholder': 'Present Branch' , 'class': 'form-control' }),
        }

class programform(forms.ModelForm):

	class Meta:
		model=program
		fields='__all__'
