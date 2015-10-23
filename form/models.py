from django.db import models

# Create your models here.

class userpost(models.Model):
	
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


	BRANCHLIST = ((a,a),(b,b),(c,c),(d,d),(e,e),(f,f),(ge,ge),(h,h),(i,i),(j,j),(k,k),(l,l),(m,m),(n,n),(om,om),(p,p),(q,q),)

	rollno = models.CharField( max_length = 9 , verbose_name ='Roll No')
	name = models.CharField(max_length = 25 ,verbose_name ='Name')
	Present_Branch = models.CharField( max_length=25 ,verbose_name ='Present Branch', choices = BRANCHLIST)

	Category = models.CharField(max_length=7, choices = CHOICELIST, default= 'General',verbose_name ='Category')
	cpi = models.DecimalField( max_digits = 2 , decimal_places = 2,verbose_name ='CPI')
	Preference_1 = models.CharField(max_length = 25,verbose_name ='Preference 1' , choices = BRANCHLIST)