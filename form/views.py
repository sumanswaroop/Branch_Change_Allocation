from django.shortcuts import render
from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib import messages
from django.template import RequestContext
from branchchange.forms import BranchChangeUsers
from form.forms import userpostform,programform
from form.models import userpost,program
from django import forms
from django.http import HttpResponse
import csv,os
import shutil
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def bchangeform(request):

    #if not logged in redirect
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    try:
        queryset =userpost.objects.get(rollno = request.user.first_name)
    except:
        queryset = None

    if request.method == 'POST':
        form = userpostform(request.POST, instance = queryset)
        if form.is_valid():
            form.save()
            return render(request , 'success.html' , {'form':form})
        else:
            print form.errors
            return render(request , 'form.html' , {'form':form})

    else:
        try:
            form = userpostform(initial = {'rollno' : request.user.first_name , 'name' : queryset.name, 'cpi': queryset.cpi, 'Present_Branch' : queryset.Present_Branch, 'Category': queryset.Category, 'Preference_1': queryset.Preference_1, 'Preference_2': queryset.Preference_2, 'Preference_3': queryset.Preference_3, 'Preference_4': queryset.Preference_4, 'Preference_5': queryset.Preference_5, 'Preference_6': queryset.Preference_6, 'Preference_7': queryset.Preference_7, 'Preference_8': queryset.Preference_8, 'Preference_9': queryset.Preference_9, 'Preference_10': queryset.Preference_10, 'Preference_11': queryset.Preference_11, 'Preference_12': queryset.Preference_12, 'Preference_13': queryset.Preference_13, 'Preference_14': queryset.Preference_14, 'Preference_15': queryset.Preference_15, 'Preference_16': queryset.Preference_16})
        except:
            form = userpostform(initial = {'rollno': request.user.first_name})
    context = {
     'form' :form,
     'queryset' :queryset

    }
    return render(request, 'form.html', context)

@login_required
def fdetail(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    try:
        queryset =userpost.objects.get(rollno = request.user.first_name)
        form = userpostform(initial = {'rollno' : request.user.first_name , 'name' : queryset.name, 'cpi': queryset.cpi, 'Present_Branch' : queryset.Present_Branch, 'Category': queryset.Category, 'Preference_1': queryset.Preference_1, 'Preference_2': queryset.Preference_2, 'Preference_3': queryset.Preference_3, 'Preference_4': queryset.Preference_4, 'Preference_5': queryset.Preference_5, 'Preference_6': queryset.Preference_6, 'Preference_7': queryset.Preference_7, 'Preference_8': queryset.Preference_8, 'Preference_9': queryset.Preference_9, 'Preference_10': queryset.Preference_10, 'Preference_11': queryset.Preference_11, 'Preference_12': queryset.Preference_12, 'Preference_13': queryset.Preference_13, 'Preference_14': queryset.Preference_14, 'Preference_15': queryset.Preference_15, 'Preference_16': queryset.Preference_16})
        return render(request, 'success.html' ,{'form' : form})
    except:
        queryset = None
        return HttpResponseRedirect('/bchangeform')

def login(request):
    c={}
    c.update(csrf(request))
    if request.user.is_authenticated():
        return HttpResponseRedirect('/bchangeform')
    return render_to_response('home.html', c, context_instance= RequestContext(request))


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password =password )

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/bchangeform')
    else:
        messages.error(request, 'Username or Password is not valid')
        return HttpResponseRedirect('/login')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return render_to_response('logout.html')

def register(request):
    if request.method == 'POST':
        form = BranchChangeUsers(request.POST)
        if form.is_valid():
            form.save()
            return render(request , 'registersuccess.html', {})
        else:
            print form.errors
    else:
        form = BranchChangeUsers()

    args = {}
    args.update(csrf(request))
    args['form'] = BranchChangeUsers()
    return render(request , 'register.html',{'form':form})
@login_required
def success(request):
    return render(request,'success.html' , {})
@login_required
def registersuccess(request):
    return render(request ,'registersuccess.html' , {})

def showprograms(request):
    if request.method=='POST':
        if request.POST.get('save') :
            if os.path.exists("input/programs.csv") :
                #os.remove("input/programs.csv")
                shutil.move("input/programs.csv","input/temp/programs.csv")
            progform=programform(request.POST)
            if progform.is_valid() :
                program.objects.all().delete()
                progs=progform.save()
                with open("input/programs.csv",'wb') as wfile:
                    writer=csv.writer(wfile,delimiter=',')
                    with open("input/programs_default.csv",'rb') as rfile:
                        reader=csv.reader(rfile,delimiter=",")
                        templist=reader[0]
                        templist[1]=str(progs.sancstrength_1)
                        templist[2]=str(progs.currstrength_1)
                        writer.write(templist)
                        templist=reader[1]
                        templist[1]=str(progs.sancstrength_2)
                        templist[2]=str(progs.currstrength_2)
                        writer.write(templist)
                        templist=reader[2]
                        templist[1]=str(progs.sancstrength_3)
                        templist[2]=str(progs.currstrength_3)
                        writer.write(templist)
                        templist=reader[3]
                        templist[1]=str(progs.sancstrength_4)
                        templist[2]=str(progs.currstrength_4)
                        writer.write(templist)
                        templist=reader[4]
                        templist[1]=str(progs.sancstrength_5)
                        templist[2]=str(progs.currstrength_5)
                        writer.write(templist)
                        templist=reader[5]
                        templist[1]=str(progs.sancstrength_6)
                        templist[2]=str(progs.currstrength_6)
                        writer.write(templist)
                        templist=reader[6]
                        templist[1]=str(progs.sancstrength_7)
                        templist[2]=str(progs.currstrength_7)
                        writer.write(templist)
                        templist=reader[7]
                        templist[1]=str(progs.sancstrength_8)
                        templist[2]=str(progs.currstrength_8)
                        writer.write(templist)
                        templist=reader[8]
                        templist[1]=str(progs.sancstrength_9)
                        templist[2]=str(progs.currstrength_9)
                        writer.write(templist)
                        templist=reader[9]
                        templist[1]=str(progs.sancstrength_10)
                        templist[2]=str(progs.currstrength_10)
                        writer.write(templist)
                        templist=reader[10]
                        templist[1]=str(progs.sancstrength_11)
                        templist[2]=str(progs.currstrength_11)
                        writer.write(templist)
                        templist=reader[11]
                        templist[1]=str(progs.sancstrength_12)
                        templist[2]=str(progs.currstrength_12)
                        writer.write(templist)
                        templist=reader[12]
                        templist[1]=str(progs.sancstrength_13)
                        templist[2]=str(progs.currstrength_13)
                        writer.write(templist)
                        templist=reader[13]
                        templist[1]=str(progs.sancstrength_14)
                        templist[2]=str(progs.currstrength_14)
                        writer.write(templist)
                        templist=reader[14]
                        templist[1]=str(progs.sancstrength_15)
                        templist[2]=str(progs.currstrength_15)
                        writer.write(templist)
                        templist=reader[15]
                        templist[1]=str(progs.sancstrength_16)
                        templist[2]=str(progs.currstrength_16)
                        writer.write(templist)
                        templist=reader[16]
                        templist[1]=str(progs.sancstrength_17)
                        templist[2]=str(progs.currstrength_17)
                        writer.write(templist)
                os.remove("input/temp/programs.csv")
                return redirect('/admin/')
            else:
                args={}
                args.update(csrf(request))
                args['form']=programform(instance=program.objects.all()[0])
                return render(request,"admin/programs.html",args)

        elif request.POST.get('back') :
            return redirect("/admin/")

    else:
        args={}
        args.update(csrf(request))
        if len(program.objects.all())>1:
            args['form']=programform(instance=program.objects.all()[0])
        else:
            args['form']=programform()
        return render(request,"admin/programs.html",args)

#views for admin are defined here

def generateoutput(request):
    print("hola")
    if request.method=='POST':
        print("59")
        if request.POST.get("output"):
            if os.path.exists("/output/output.csv"):
                os.remove("/output/output.csv")
            if os.path.exists("/output/stats.csv"):
                os.remove("/output/stats.csv")                
            if request.FILES.get('input') and request.FILES.get('programs') :
                if os.path.exists("input/input.csv") :
                    os.remove("input/input.csv")
                if os.path.exists("input/programs.csv"):
                    shutil.move("input/programs.csv","input/temp/programs.csv")
                    #os.remove("input/programs.csv")
                ifile=request.FILES.get('input')
                pfile=request.FILES.get('programs')
                with open("input/input.csv","wb") as inputfile :
                    with open("input/programs.csv","wb") as programfile:  
                        reader1=csv.reader(ifile,delimiter=",")
                        writer1=csv.writer(inputfile,delimiter=",")
                        reader2=csv.reader(pfile,delimiter=",")
                        writer2=csv.writer(programfile,delimiter=",")
                        for x  in reader1:
                            writer1.writerow(x)
                        for x in reader2:
                            writer2.writerow(x)
                #genrearted outputfiles
   
                #call java function here
                #os.remove("input/programs.csv")
                #shutil.move("input/programs.csv","input/temp/programs.csv")
            else:
                if os.path.exists("input/input.csv") :
                    os.remove("input/input.csv")
                #if os.path.exists("input/programs.csv"):
                #   os.remove("input/programs.csv")

                # genereate a csv file with present input data an
                print("67")
                #change here
                with open('input/input.csv','wb') as csvfile:
                    print("98")
                    writer=csv.writer(csvfile,delimiter=',')
                    #writer.writerow(['RollNo', 'Name', 'CurrentBranch', 'CPI', 'Category', 'Options'])
                    for x in userpost.objects.all() :

                        row=[]
                        row.append(str(x.rollno))
                        row.append(str(x.name))
                        row.append(str(x.Present_Branch))
                        row.append(float(x.cpi))
                        row.append(str(x.Category))
                        row.append(str(x.Preference_1))
                        row.append(str(x.Preference_2))
                        row.append(str(x.Preference_3))
                        row.append(str(x.Preference_4))
                        row.append(str(x.Preference_5))
                        row.append(str(x.Preference_6))
                        row.append(str(x.Preference_7))
                        row.append(str(x.Preference_8))
                        row.append(str(x.Preference_9))
                        row.append(str(x.Preference_10))
                        row.append(str(x.Preference_11))
                        row.append(str(x.Preference_12))
                        row.append(str(x.Preference_13))
                        row.append(str(x.Preference_14))
                        row.append(str(x.Preference_15))
                        row.append(str(x.Preference_16))

                        writer.writerow(row)

                        address='input/input.csv'
                    #os.system.
            #call java functions here with input file of address=address
            #programs file "input/programs.csv"
            #assuming i  have the output.csv file
            #
            #os.system("cd input/")
            os.chdir("input/")
            print(os.getcwd())
            os.system("java Java/Main")
            if os.path.exists("./output.csv") :
                shutil.move("./output.csv","../output/output.csv")
                shutil.move("./stats.csv","../output/stats.csv")
            else:
                print("error in genereating file")
            #os.system("cd ..")
            os.chdir("..")
            print(os.getcwd())
            #os.remove("input/input.csv")
            if os.path.exists("input/temp/programs.csv") :
                os.remove("input/programs.csv")
                shutil.move("input/temp/programs.csv","input/programs.csv")
            #shutil.move("input/output.csv","output/output.csv")    
            with open('output/output.csv','rb') as ocsv:
                reader=csv.reader(ocsv,delimiter=',')
                #reader=reader[1:]
                #print(reader)
                args={}
                args['output']=reader
                return render(request,'output.html',args)

    return redirect('/admin/')

def generatestats(request):
    if request.method=="POST":
        if request.POST.get('stats'):
            if os.path.exists("output/stats.csv"):
                with open('output/stats.csv','rb') as ocsv:
                    reader=csv.reader(ocsv,delimiter=',')
                    #print(list(reader))
                    #reader=reader[1:]
                    args={}
                    args['output']=reader
                    return render(request,'stats.html',args)
            else:
                args={}
                args.update(csrf(request))
                args['error']="File does not exists"
                return render(request,'error.html',args)
    else:
        return redirect('/admin/')                                    
