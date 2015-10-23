from django import forms
from form.models import userpost


class userpostform(forms.ModelForm):
	g='General'
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

	Category = forms.ChoiceField(choices=CHOICELIST, required=True ,widget=forms.Select(attrs={'class':'form-control'}))
	Present_Branch = forms.ChoiceField(choices=BRANCHLIST, required=True ,widget=forms.Select(attrs={'class':'form-control'}))
	Preference_1 = forms.ChoiceField(choices=BRANCHLIST, required=True ,widget=forms.Select(attrs={'class':'form-control'}))
	
	
	
	class Meta:
		model = userpost
		fields = ('rollno' ,'name' ,'Category' ,'Present_Branch', 'cpi' ,'Preference_1')
		widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name' , 'class': 'form-control' }),
            'rollno': forms.TextInput(attrs={'placeholder': '15XXXXXXX Roll' , 'class': 'form-control' }),
            'cpi': forms.TextInput(attrs={'placeholder': 'CPI in [0:10]' , 'class': 'form-control' }),
            'pbranch': forms.TextInput(attrs={'placeholder': 'Present Branch' , 'class': 'form-control' }),
        }

