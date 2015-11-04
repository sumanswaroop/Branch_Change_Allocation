from django.db import models

# Create your models here.

class userpost(models.Model):

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

	rollno = models.CharField( max_length = 9 , verbose_name ='Roll No')
	name = models.CharField(max_length = 25 ,verbose_name ='Name')
	Present_Branch = models.CharField( max_length=25 ,verbose_name ='Present Branch', choices = BRANCHLIST,null=True,blank=False)

	Category = models.CharField(max_length=7, choices = CHOICELIST, default= 'General',verbose_name ='Category')
	cpi = models.DecimalField( max_digits = 5 , decimal_places = 2,verbose_name ='CPI')
	Preference_1 = models.CharField(max_length = 25,verbose_name ='Preference 1' , choices = BRANCHLIST,null=True,blank=False)
	Preference_2 = models.CharField(max_length = 25,verbose_name ='Preference 2' , choices = BRANCHLIST,null=True,blank=True)
	Preference_3 = models.CharField(max_length = 25,verbose_name ='Preference 3' , choices = BRANCHLIST,null=True,blank=True)
	Preference_4 = models.CharField(max_length = 25,verbose_name ='Preference 4' , choices = BRANCHLIST,null=True,blank=True)
	Preference_5 = models.CharField(max_length = 25,verbose_name ='Preference 5' , choices = BRANCHLIST,null=True,blank=True)
	Preference_6 = models.CharField(max_length = 25,verbose_name ='Preference 6' , choices = BRANCHLIST,null=True,blank=True)
	Preference_7 = models.CharField(max_length = 25,verbose_name ='Preference 7' , choices = BRANCHLIST,null=True,blank=True)
	Preference_8 = models.CharField(max_length = 25,verbose_name ='Preference 8' , choices = BRANCHLIST,null=True,blank=True)
	Preference_9 = models.CharField(max_length = 25,verbose_name ='Preference 9' , choices = BRANCHLIST,null=True,blank=True)
	Preference_10 = models.CharField(max_length = 25,verbose_name ='Preference 10' , choices = BRANCHLIST,null=True,blank=True)
	Preference_11 = models.CharField(max_length = 25,verbose_name ='Preference 11' , choices = BRANCHLIST,null=True,blank=True)
	Preference_12 = models.CharField(max_length = 25,verbose_name ='Preference 12' , choices = BRANCHLIST,null=True,blank=True)
	Preference_13 = models.CharField(max_length = 25,verbose_name ='Preference 13' , choices = BRANCHLIST,null=True,blank=True)
	Preference_14 = models.CharField(max_length = 25,verbose_name ='Preference 14' , choices = BRANCHLIST,null=True,blank=True)
	Preference_15 = models.CharField(max_length = 25,verbose_name ='Preference 15' , choices = BRANCHLIST,null=True,blank=True)
	Preference_16 = models.CharField(max_length = 25,verbose_name ='Preference 16' , choices = BRANCHLIST,null=True,blank=True)


	def __unicode__(self):
		return self.rollno




class program(models.Model):

	name=models.CharField(max_length=25,null=True,blank=True)
	sancstrength_1=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_2=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_3=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_4=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_5=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_6=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_7=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_8=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_9=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_10=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_11=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_12=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_13=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_14=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_15=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_16=models.PositiveIntegerField(null=True,blank=True,default=0)
	sancstrength_17=models.PositiveIntegerField(null=True,blank=True,default=0)

	currstrength_1=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_2=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_3=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_4=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_5=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_6=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_7=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_8=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_9=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_10=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_11=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_12=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_13=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_14=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_15=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_16=models.PositiveIntegerField(null=True,blank=True,default=0)
	currstrength_17=models.PositiveIntegerField(null=True,blank=True,default=0)


	def __unicode__(self):
		return self.name
