from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request,'./myapp/index.html')

def about(request):
    return render(request,'./myapp/about.html')

def contact(request):
    return render(request,'./myapp/contact.html')

def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, password=pwd, utype='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')

def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,password=opasswd,utype='admin')
            if ul is not None:
                ul.password=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)

from .models import type_master


def admin_type_master_add(request):
    if request.method == 'POST':
        type_name = request.POST.get('type_name')
        tm = type_master(type_name=type_name)
        tm.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/admin_type_master_add.html', context)
    else:
        return render(request, './myapp/admin_type_master_add.html')


def admin_type_master_edit(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        type_name = request.POST.get('type_name')
        tm = type_master.objects.get(id=int(s_id))

        tm.type_name = type_name
        tm.save()
        msg = 'Record Updated'
        tm_l = type_master.objects.all()
        context = {'type_list': tm_l, 'msg': msg}
        return render(request, './myapp/admin_type_master_view.html', context)
    else:
        id = request.GET.get('id')
        tm = type_master.objects.get(id=int(id))
        context = {'type_name': tm.type_name, 's_id': tm.id}
        return render(request, './myapp/admin_type_master_edit.html',context)


def admin_type_master_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    tm = type_master.objects.get(id=int(id))
    tm.delete()
    msg = 'Record Deleted'
    tm_l = type_master.objects.all()
    context = {'type_list': tm_l, 'msg':msg}
    return render(request, './myapp/admin_type_master_view.html',context)


def admin_type_master_view(request):
    tm_l = type_master.objects.all()
    context = {'type_list':tm_l}
    return render(request, './myapp/admin_type_master_view.html',context)


def admin_user_view(request):
    ul_l = user_login.objects.filter(utype='user')

    tm_l = []
    for u in ul_l:
        ud = user_details.objects.get(user_id=u.id)
        tm_l.append(ud)

    context = {'user_list':tm_l,'type':'Reporter Details'}
    return render(request, './myapp/admin_user_view.html',context)

def admin_guest_view(request):
    ul_l = user_login.objects.filter(utype='guest')

    tm_l = []
    for u in ul_l:
        ud = user_details.objects.get(user_id=u.id)
        tm_l.append(ud)

    context = {'user_list':tm_l,'type':'User Details'}
    return render(request, './myapp/admin_user_view.html',context)

from .models import keywords_master

def admin_keywords_master_add(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        km = keywords_master(keywords=keywords)
        km.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/admin_keywords_master_add.html', context)
    else:
        return render(request, './myapp/admin_keywords_master_add.html')


def admin_keywords_master_edit(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        keywords = request.POST.get('keywords')
        km = keywords_master.objects.get(id=int(s_id))

        km.keywords = keywords
        km.save()
        msg = 'Record Updated'
        km_l = keywords_master.objects.all()
        context = {'keywords_list': km_l, 'msg': msg}
        return render(request, './myapp/admin_keywords_master_view.html', context)
    else:
        id = request.GET.get('id')
        km = keywords_master.objects.get(id=int(id))
        context = {'keywords': km.keywords, 's_id': km.id}
        return render(request, './myapp/admin_keywords_master_edit.html',context)


def admin_keywords_master_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    km = keywords_master.objects.get(id=int(id))
    km.delete()
    msg = 'Record Deleted'
    km_l = keywords_master.objects.all()
    context = {'keywords_list': km_l, 'msg':msg}
    return render(request, './myapp/admin_keywords_master_view.html',context)


def admin_keywords_master_view(request):
    km_l = keywords_master.objects.all()
    context = {'keywords_list':km_l}
    return render(request, './myapp/admin_keywords_master_view.html',context)


from .models import pic_pool
from django.core.files.storage import FileSystemStorage
from datetime import datetime

def admin_pic_pool_add(request):
    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        pic = fs.save(u_file.name, u_file)
        type_id = int(request.POST.get('type_id'))

        pp = pic_pool(type_id=type_id,pic=pic)
        pp.save()
        tm_l = type_master.objects.all()
        context = {'type_list': tm_l,'msg': 'Record Added'}
        return render(request, './myapp/admin_pic_pool_add.html', context)
    else:
        tm_l = type_master.objects.all()
        context = {'type_list': tm_l}
        return render(request, './myapp/admin_pic_pool_add.html',context)


def admin_pic_pool_delete(request):

    id = request.GET.get('id')
    print('id = '+id)
    pp = pic_pool.objects.get(id=int(id))
    pp.delete()
    msg = 'Record Deleted'
    tm_l = type_master.objects.all()
    tml = {}
    for tm in tm_l:
        tml[tm.id] = tm.type_name

    pp_l = pic_pool.objects.all()
    context = {'pic_list': pp_l,'type_list': tml,'msg':msg}
    return render(request, './myapp/admin_pic_pool_view.html',context)

def admin_pic_pool_view(request):
    tm_l = type_master.objects.all()
    tml = {}
    for tm in tm_l:
        tml[tm.id] = tm.type_name
    pp_l = pic_pool.objects.all()
    context = {'pic_list': pp_l, 'type_list': tml}
    return render(request, './myapp/admin_pic_pool_view.html', context)

from .models import label_master
def admin_label_master_add(request):
    if request.method == 'POST':
        label = request.POST.get('label')
        cm = label_master(label=label)
        cm.save()
        return render(request, 'myapp/admin_label_master_add.html')

    else:
        return render(request, 'myapp/admin_label_master_add.html')

def admin_label_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = label_master.objects.get(id=int(id))
    nm.delete()

    nm_l = label_master.objects.all()
    context ={'label_list':nm_l}
    return render(request,'myapp/admin_label_master_view.html',context)

def admin_label_master_view(request):
    nm_l = label_master.objects.all()
    context ={'label_list':nm_l}
    return render(request,'myapp/admin_label_master_view.html',context)

from .topic_classification import TopicClassification
from project.settings import BASE_DIR
import os

from .models import data_set
def admin_data_set_add(request):
    if request.method == 'POST':
        label_id=int(request.POST.get('label_id'))
        data_file=request.POST.get('data_file')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status='ok'

        cm = data_set(label_id=label_id,data_file=data_file,dt=dt,tm=tm,status=status)
        cm.save()

        ##########training model############
        data_file_path = os.path.join(BASE_DIR, 'data/data_set.csv')
        #os.remove(data_file_path)

        obj_list = data_set.objects.all()
        f = open(data_file_path, "w")
        f.write('text,label')
        f.write("\n")
        for obj in obj_list:
            lb = label_master.objects.get(id=obj.label_id)
            f.write(f'{obj.data_file},{lb.label}')
            f.write("\n")
        f.close()
        data_file_path = os.path.join(BASE_DIR, 'data/data_set.csv')
        data_file_label_path = os.path.join(BASE_DIR, 'data/data_set_label.dat')
        tfid_file_path = os.path.join(BASE_DIR, 'data/data_set_tfid.dat')
        model_file_path = os.path.join(BASE_DIR, 'data/data_set_svm.model')

        obj = TopicClassification()
        txt_result = obj.text_processing(data_file_path,data_file_label_path)
        obj.train_model(txt_result,tfid_file_path,model_file_path,'svm')
        ################
        nm_l = label_master.objects.all()
        context = {'label_list': nm_l,'msg':'Record Added'}
        return render(request, 'myapp/admin_data_set_add.html',context)

    else:
        nm_l = label_master.objects.all()
        for nm in nm_l:
            print(nm.id)
        context = {'label_list': nm_l, 'msg': ''}
        return render(request, 'myapp/admin_data_set_add.html',context)

def admin_data_set_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = data_set.objects.get(id=int(id))
    nm.delete()

    nm_l = data_set.objects.all()
    cmd = {}
    for nm in nm_l:
        lb = label_master.objects.get(id=nm.label_id)
        cmd[nm.label_id] = lb.label

    context ={'data_list':nm_l,'label_list':cmd,'msg':'Record Deleted'}
    return render(request,'myapp/admin_data_set_view.html',context)

def admin_data_set_view(request):
    nm_l = data_set.objects.all()
    cmd = {}
    for nm in nm_l:
        lb = label_master.objects.get(id=nm.label_id)
        cmd[nm.label_id] = lb.label

    context = {'data_list': nm_l, 'label_list': cmd, 'msg': ''}
    return render(request, 'myapp/admin_data_set_view.html', context)

def admin_posts_all(request):
    user_list ={}
    ud_l = user_details.objects.all()
    for ud in ud_l:
        user_list[ud.user_id] = ud.profile_name
    up_l = user_posts.objects.all()
    context = {'user_list':user_list,'report_list': up_l}
    return render(request, './myapp/admin_posts_view2.html',context)

########USER#############
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, password=passwd,utype='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        profile_name = request.POST.get('profile_name')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = '1234'
        uname=email
        status = "new"

        ul = user_login(uname=uname, password=password, utype='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, addr=addr, pin=pin, contact=contact,
                               status=status,email=email,profile_name=profile_name,dob=dob )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')

def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)

from .models import user_posts
from .text_algo import get_word_set, remove_duplicates, list_to_string
from .image_algo import pic_search
def user_posts_add(request):
    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)

        pic = path
        post_type = request.POST.get('post_type')
        msg = request.POST.get('msg')

        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = "PENDING"
        user_id = int(request.session['user_id'])
        ##################Text Algo########################################
        c_w = get_word_set(msg)
        print(c_w)
        f_w = remove_duplicates(c_w)
        status = list_to_string(f_w)
        ##################################################################
        ################## Image Algo #####################################
        pp_l = pic_pool.objects.all()
        pic_list = []
        cat_list = []
        for pp in pp_l:
            pic_list.append(pp.pic)
            cat_list.append(pp.type_id)
        selfile,selcat = pic_search(pic_list=pic_list,cat_list=cat_list,pic_path=pic)
        tmaster = type_master.objects.get(id=selcat)
        status  = status + ',' + tmaster.type_name
        #################ML ALGO####################
        obj = TopicClassification()
        result = obj.input_text_processing(msg)
        data_file_path = os.path.join(BASE_DIR, 'data/data_set.csv')
        data_file_label_path = os.path.join(BASE_DIR, 'data/data_set_label.dat')
        tfid_file_path = os.path.join(BASE_DIR, 'data/data_set_tfid.dat')
        model_file_path = os.path.join(BASE_DIR, 'data/data_set_svm.model')

        model = obj.load_data(model_file_path)
        Tfidf_vect = obj.load_data(tfid_file_path)
        p = obj.get_prediction(model, result, Tfidf_vect)
        label = obj.load_data(data_file_label_path)
        label = sorted(label)
        print(f'result = {label[p[0]]}')
        final_label = label[p[0]]
        status = status + ',' + final_label
        ###############################################



        up = user_posts(user_id=user_id,pic=pic,post_type=post_type,msg=msg,dt=dt,tm=tm,status=status)
        up.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/user_posts_add.html', context)
    else:
        return render(request, './myapp/user_posts_add.html')

def user_posts_delete(request):
    id = request.GET.get('id')
    print('id = ' + id)
    up = user_posts.objects.get(id=int(id))
    up.delete()

    user_id = int(request.session['user_id'])
    up_l = user_posts.objects.filter(user_id=user_id)
    context = {'report_list': up_l,'msg':'Post Deleted'}
    return render(request, './myapp/user_posts_view.html',context)


def user_posts_view(request):
    user_id = int(request.session['user_id'])
    up_l = user_posts.objects.filter(user_id=user_id)
    context = {'report_list': up_l}
    return render(request, './myapp/user_posts_view.html',context)


def user_posts_search(request):
    if request.method == 'POST':
        user_id = int(request.session['user_id'])
        key = request.POST.get('key')
        user_list = {}
        ud_l = user_details.objects.all()
        for ud in ud_l:
            user_list[ud.user_id] = ud.profile_name
        up_l = user_posts.objects.filter(status__contains=key)
        context = {'user_list': user_list, 'report_list': up_l}
        return render(request, './myapp/user_posts_view2.html', context)
    else:
        return render(request, 'myapp/user_product_search.html')



def user_posts_all(request):
    user_list ={}
    ud_l = user_details.objects.all()
    for ud in ud_l:
        user_list[ud.user_id] = ud.profile_name
    up_l = user_posts.objects.all()
    context = {'user_list':user_list,'report_list': up_l}
    return render(request, './myapp/user_posts_view2.html',context)


######## GUEST #############
from .models import user_details

def guest_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, password=passwd,utype='guest')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            return render(request, 'myapp/guest_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/guest_login.html',context)
    else:
        return render(request, 'myapp/guest_login.html')

def guest_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/guest_home.html',context)

def guest_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        profile_name = request.POST.get('profile_name')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = '1234'
        uname=email
        status = "new"

        ul = user_login(uname=uname, password=password, utype='guest')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, addr=addr, pin=pin, contact=contact,
                               status=status,email=email,profile_name=profile_name,dob=dob )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/guest_login.html',context)

    else:
        return render(request, 'myapp/guest_details_add.html')

def guest_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/guest_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/guest_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/guest_changepassword.html', context)
    else:
        return render(request, './myapp/guest_changepassword.html')

def guest_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return guest_login_check(request)
    else:
        return guest_login_check(request)

from .models import user_posts
from .text_algo import get_word_set, remove_duplicates, list_to_string
from .image_algo import pic_search


def guest_posts_search(request):
    if request.method == 'POST':
        user_id = int(request.session['user_id'])
        key = request.POST.get('key')
        user_list = {}
        ud_l = user_details.objects.all()
        for ud in ud_l:
            user_list[ud.user_id] = ud.profile_name
        up_l = user_posts.objects.filter(status__contains=key)
        context = {'user_list': user_list, 'report_list': up_l}
        return render(request, './myapp/guest_posts_view2.html', context)
    else:
        return render(request, 'myapp/guest_product_search.html')



def guest_posts_all(request):
    user_list ={}
    ud_l = user_details.objects.all()
    for ud in ud_l:
        user_list[ud.user_id] = ud.profile_name
    up_l = user_posts.objects.all()
    context = {'user_list':user_list,'report_list': up_l}
    return render(request, './myapp/guest_posts_view2.html',context)

from .models import user_review
def guest_news_review_add(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        user_id = request.session['user_id']

        msg = request.POST.get('msg')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'ok'
        pr = user_review(post_id=int(post_id),user_id=int(user_id),msg=msg,
                            dt=dt,tm=tm)
        pr.save()

        context = {'msg':'Review added','post_id':post_id}
        return render(request, 'myapp/guest_news_review_add.html',context)

    else:
        post_id = request.GET.get('post_id')
        context = {'msg':'','post_id':post_id}
        return render(request, 'myapp/guest_news_review_add.html',context)

def guest_news_review_delete(request):
    id = request.GET.get('id')
    try:
        post_id = request.GET.get('post_id')
        print("id="+id)
        pp = user_review.objects.get(id=int(id))
        pp.delete()
        user_id = request.session['user_id']
        post_id = request.GET.get('post_id')
        pr_l = user_review.objects.filter(post_id=int(post_id), user_id=int(user_id))
        context = {'review_list': pr_l, 'post_id': post_id, 'msg': 'Review deleted'}
        return render(request, 'myapp/guest_news_review_view.html', context)
    except:
        user_id = request.session['user_id']
        post_id = request.GET.get('post_id')
        pr_l = user_review.objects.filter(post_id=int(post_id), user_id=int(user_id))
        context = {'review_list': pr_l, 'post_id': post_id, 'msg': 'Review deleted'}
        return render(request, 'myapp/guest_news_review_view.html', context)


def guest_news_review_view(request):
    user_id=request.session['user_id']
    post_id = request.GET.get('post_id')
    pr_l = user_review.objects.filter(post_id=int(post_id),user_id=int(user_id))
    context = {'review_list': pr_l, 'post_id': post_id, 'msg': ''}
    return render(request, 'myapp/guest_news_review_view.html', context)

def guest_news_allreview_view(request):
    post_id = request.GET.get('post_id')
    pr_l = user_review.objects.filter(post_id=post_id)
    cmd={}
    umd = {}
    all_sentiment =list()
    for pr in pr_l:
        uobj = user_login.objects.get(id=pr.user_id)
        udobj = user_details.objects.get(email=uobj.uname)
        umd[pr.user_id] = f'{udobj.fname} {udobj.lname}'


    context = {'review_list': pr_l,'user_list': umd,'sentiment_list': cmd, 'post_id': post_id, 'msg': ''}
    return render(request, 'myapp/guest_news_allreview_view.html', context)


