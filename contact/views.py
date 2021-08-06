from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.forms import UserCreationForm




def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search')
    if search_input:
        contacts = Contact.objects.filter(first_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ""
    return render(request, 'index.html', {'contacts':contacts , 'search_input': search_input} )
  

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
           
    return render(request, '/', {'form': form})


def addContact(request):
    if request.method == 'POST':
        newContacts = Contact(
            first_name = request.POST['firstName'],
            last_name = request.POST['lastName'],
            phone = request.POST['phone'],
            email = request.POST['email'],
            address = request.POST['address']
        
        )
        newContacts.save()
        
        ## redirect to home page
        return redirect ('/')
    return render(request, 'new.html')
    
    
def contactProfile(request,pk):
    contact = Contact.objects.get(id=pk)
    return render(request,'contact-profile.html', {'contact' : contact})
    

def login(request):
    
    username = request.POST.get('user')
    password = request.POST.get('pw')
    return render(request, 'index.html', {'username' : username})
    
def logout(request):
    
    return  render(request,'index.html')
   
def deleteContact(request,pk):
    
    if request.method == 'POST':
        contact = Contact.objects.get(id=pk)
    
    
        contact.delete()
        return redirect('/')
    return render(request, 'contact-profile.html', {'contact':contact})
    