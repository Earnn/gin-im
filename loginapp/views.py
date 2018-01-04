from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import SignUpForm,ProfileForm
from mainapp.models import *
from django.views.generic.edit import UpdateView
# change password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import Http404
def handler404(request):
    print("404")
    response = render_to_response('404.html',{},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler403(request):
    print("403")
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response

def handler400(request):
    print("400")
    response = render_to_response('400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response

def handler500(request):
    print("500")
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def home(request):
    return render(request, 'home.html',{'username': request.user.username})

# from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

# @login_required
# def profile(request):
#     love_list = []
#     order_list =[]
#     try:
#         p = Profile.objects.get(user = request.user)
#         print (p.name)
#         print (p.picture.url)
#         form = ProfileForm(initial={'name': p.name,'image':p.picture.url,'phone':p.phone_number,'address':p.address})
#         form.fields['name'].widget.attrs['placeholder'] = p.name
#         # form.fields['image'].widget.attrs['placeholder'] = p.picture.url
#         form.fields['phone'].widget.attrs['placeholder'] = p.phone_number
#         form.fields['address'].widget.attrs['placeholder'] = p.address

#         if request.method == 'POST':
#             form = ProfileForm(request.POST, request.FILES)
#             if form.is_valid():
#                 print("Earn")
#                 profile_update = Profile.objects.filter(user=request.user).update(name=form.cleaned_data['name'],
#                     picture= request.FILES['image'],
#                     address=form.cleaned_data['address'],
#                      phone_number=form.cleaned_data['phone'])
#                 p = Profile.objects.get(user=request.user)
#                 p.picture = request.FILES['image']
#                 p.save()
#                 # form.save()
               
#                 # login(request, user)
#                 return redirect('profile')
       
#         love = {'name' : '' , 'img':''}   
      
#         user = request.user
#         store = Store.objects.filter(likes=user)
#         for l in store:
#             love['name'] = l.name
#             love['img'] = l.image
#             love_list.append(love)
       

#         try :
#             reviews = Review.objects.filter(user=request.user)
#             temp = { 'rating_color': 0,'rating_no_color': 0, }
#             rate = []
#             profile_picture = []
#             for i in reviews:
#                 temp['rating_color'] = i.rating
#                 temp['rating_no_color'] = 5 - temp['rating_color']
#                 rate.append(temp)
#                 profile_picture.append(Profile.objects.get(user=i.user).picture.url)

#             out = zip(reviews,rate,profile_picture)
#             mobile_out = zip(reviews,rate,profile_picture)
#             # review

#         except :
#             raise

#         try :
#             orders = Order.objects.filter(user=request.user)
#             for i in orders:
#                 temp = {'id':0,'name_s':"",'menu_amount':[],'date':None}
#                 temp['id'] = i.id
#                 print(i.store.id)
#                 s = Store.objects.get(id=i.store.id) 
#                 temp['name_s'] = s.name
#                 temp['date'] = i.date

#                 menu_list = []
#                 amount_list = []
#                 keys = ['menu','amount']
#                 for m,a in zip(i.menu,i.amount):
#                     ma = {'menu':Menu.objects.get(id=m),'amount':a}
#                     temp['menu_amount'].append(ma)
#         #             menu_list.append(Menu.objects.get(id=m))
#         #             amount_list.append(a)
                    
#         # { row.SITE_NAME : row.LOOKUP_TABLE for row in cursor }
                
#         #         temp['menu_amount'](dict(zip(menu_list, amount_list)))
            

#                 order_list.append(temp)

#         except :
#             raise


#     except Profile.DoesNotExist:
#             raise



#     return render(request, 'profile.html',{'form': form,'username': request.user.username,'person':p,'love_list':love_list,'order_list':order_list,'out':out,'mobile_out':mobile_out})

# @login_required
# def profile_store(request):
#     love_list = []
#     order_list =[]
#     try:
#         p = Profile.objects.get(user = request.user)
#         print (p.name)
#         print (p.picture.url)
#         form = ProfileForm(initial={'name': p.name,'image':p.picture.url,'phone':p.phone_number,'address':p.address})
#         form.fields['name'].widget.attrs['placeholder'] = p.name
#         form.fields['phone'].widget.attrs['placeholder'] = p.phone_number
#         form.fields['address'].widget.attrs['placeholder'] = p.address

#         if request.method == 'POST':
#             form = ProfileForm(request.POST, request.FILES)
#             if form.is_valid():
#                 print("Earn")
#                 profile_update = Profile.objects.filter(user=request.user).update(name=form.cleaned_data['name'],
#                     picture= request.FILES['image'],
#                     address=form.cleaned_data['address'],
#                      phone_number=form.cleaned_data['phone'])
#                 p = Profile.objects.get(user=request.user)
#                 p.picture = request.FILES['image']
#                 p.save()
   
#                 return redirect('profile')
       
#         love = {'name' : '' , 'img':''}   
      
#         user = request.user
#         store = Store.objects.filter(likes=user)
#         for l in store:
#             love['name'] = l.name
#             love['img'] = l.image
#             love_list.append(love)
       

#         try :
#             reviews = Review.objects.filter(user=request.user)
#             temp = { 'rating_color': 0,'rating_no_color': 0, }
#             rate = []
#             profile_picture = []
#             for i in reviews:
#                 temp['rating_color'] = i.rating
#                 temp['rating_no_color'] = 5 - temp['rating_color']
#                 rate.append(temp)
#                 profile_picture.append(Profile.objects.get(user=i.user).picture.url)

#             out = zip(reviews,rate,profile_picture)
#             mobile_out = zip(reviews,rate,profile_picture)
#             # review

#         except :
#             raise

#         try :
#             orders = Order.objects.filter(user=request.user)
#             for i in orders:
#                 temp = {'id':0,'name_s':"",'menu_amount':[],'date':None}
#                 temp['id'] = i.id
#                 print(i.store.id)
#                 s = Store.objects.get(id=i.store.id) 
#                 temp['name_s'] = s.name
#                 temp['date'] = i.date

#                 menu_list = []
#                 amount_list = []
#                 keys = ['menu','amount']
#                 for m,a in zip(i.menu,i.amount):
#                     ma = {'menu':Menu.objects.get(id=m),'amount':a}
#                     temp['menu_amount'].append(ma)
#         #             menu_list.append(Menu.objects.get(id=m))
#         #             amount_list.append(a)
                    
#         # { row.SITE_NAME : row.LOOKUP_TABLE for row in cursor }
                
#         #         temp['menu_amount'](dict(zip(menu_list, amount_list)))
            

#                 order_list.append(temp)

#         except :
#             raise


#     except Profile.DoesNotExist:
#             raise



#     return render(request, 'profile_store.html',{'form': form,'username': request.user.username,'person':p,'love_list':love_list,'order_list':order_list,'out':out,'mobile_out':mobile_out})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            print("Earn")
           
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            p = Profile(picture = request.FILES['image'],user=user,name=username,email=form.cleaned_data.get('email'))
            p.save()
            # login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    check = Profile.objects.get(user=request.user)
    print(check.status)
    love_list = []
    order_list =[]
    try:
        p = Profile.objects.get(user = request.user)
        print (p.name)
        print (p.picture.url)
        form = ProfileForm(initial={'name': p.name,'image':p.picture.url,'phone':p.phone_number,'address':p.address})
        form.fields['name'].widget.attrs['placeholder'] = p.name
            # form.fields['image'].widget.attrs['placeholder'] = p.picture.url
        form.fields['phone'].widget.attrs['placeholder'] = p.phone_number
        form.fields['address'].widget.attrs['placeholder'] = p.address

        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
              
                profile_update = Profile.objects.filter(user=request.user).update(name=form.cleaned_data['name'],
                picture= request.FILES['image'],
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone'])
                p = Profile.objects.get(user=request.user)
                p.picture = request.FILES['image']
                p.save()
                
                return redirect('profile')
           
        love = {'name' : '' , 'img':''}   
          
        user = request.user
        store = Store.objects.filter(likes=user)
        for l in store:
            love['name'] = l.name
            love['img'] = l.image
            love_list.append(love)
           

        try :
            reviews = Review.objects.filter(user=request.user)
            temp = { 'rating_color': 0,'rating_no_color': 0, }
            rate = []
            profile_picture = []
            for i in reviews:
                temp['rating_color'] = i.rating
                temp['rating_no_color'] = 5 - temp['rating_color']
                rate.append(temp)
                profile_picture.append(Profile.objects.get(user=i.user).picture.url)

            out = zip(reviews,rate,profile_picture)
            mobile_out = zip(reviews,rate,profile_picture)
              
        except Exception as ex:
            messages.error(request, ex)
            raise Http404()
         
        try :
            orders = Order.objects.filter(user=request.user)
            for i in orders:
                temp = {'id':0,'name_s':"",'menu_amount':[],'date':None}
                temp['id'] = i.id
                print(i.store.id)
                s = Store.objects.get(id=i.store.id) 
                temp['name_s'] = s.name
                temp['date'] = i.date

                menu_list = []
                amount_list = []
                keys = ['menu','amount']
                for m,a in zip(i.menu,i.amount):
                    ma = {'menu':Menu.objects.get(id=m),'amount':a}
                    temp['menu_amount'].append(ma)
   
                order_list.append(temp)

        except :
            raise


    except Profile.DoesNotExist:
            raise

    if check.status == 'store' :

        return render(request, 'profile_store.html',{'form': form,'username': request.user.username,
            'person':p,'love_list':love_list,'order_list':order_list,'out':out,
            'mobile_out':mobile_out})
    else :
    

        return render(request, 'profile.html',{'form': form,'username': request.user.username,
            'person':p,'love_list':love_list,'order_list':order_list,'out':out,
            'mobile_out':mobile_out})






