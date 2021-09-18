from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Comment, Contact, Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import ConttactForm, Customusercreation, Customerlogin,PostForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from Myblog.settings import EMAIL_HOST_USER


def index(request):
    myposts = Post.objects.all()
    print(myposts)
    paginator = Paginator(myposts, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/newblog.html', {"posts": posts})


def aboutpost(request, myid):

    myidpost = Post.objects.filter(p_id=myid)
    comments = Comment.objects.filter(postsno=myid, parent=None)
    print(comments)
    replies = Comment.objects.filter(postsno=myid).exclude(parent=None)

    mydict = {}

    for c in comments:
        replies = Comment.objects.filter(postsno=myid).exclude(parent=None)
        print(replies)

        if len(replies) > 0:

            replist = []
            for r in replies:

                if (r.parent.sno == c.sno):

                    replist.append(r)
                    mydict[c] = replist
                    print(mydict)

            if c not in mydict:
                mydict[c] = "no"

        else:

            mydict[c] = "no"
            print(mydict)

    print(mydict)

    if len(comments) != 0:
        cmlist = comments
        # print(cmlist)

    else:
        cmlist = []

    # print(myidpost)
    return render(request, 'blog/aboutpost.html', {"posts": myidpost[0], "mydict": mydict})


def postcom(request):
    if request.method == "POST":
        check = request.POST.get("check")
        comno = request.POST.get("comno")
        mycom = request.POST.get("postcom", "default")
        sno = request.POST.get("postsno", "default")
        post = Post.objects.get(p_id=sno)
        # print(mycom, sno)
        if check == "parent":
            comment = Comment(postcomment=mycom,
                              user=request.user, post=post, postsno=sno)
        if check == "child":
            parent = Comment.objects.get(sno=comno)
            comment = Comment(postcomment=mycom, user=request.user,
                              post=post, postsno=sno, parent=parent)

        comment.save()
        return redirect(f"/aboutpost/{sno}/")


def signup(request):
    fm = Customusercreation()
    if request.method == "POST":
        fm = Customusercreation(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(
                request, "You have successfully registered.Now you can login.")
            return redirect("/")
    return render(request, "blog/signup.html", {"form": fm})


def handlelogin(request):
    fm = Customerlogin()
    if request.method == "POST":
        fm = Customerlogin(request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data["username"]
            psk = fm.cleaned_data["password"]
            print(uname)
            user = authenticate(username=uname, password=psk)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect("/")
    return render(request, "blog/login.html", {"form": fm})


def handlelogout(request):
    logout(request)
    messages.success(request, "You Successfully Logged Out")
    return redirect('/')


def contact(request):
    fm = ConttactForm(label_suffix="", auto_id=True, )

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You must have logged in")
            return redirect("/contact/")

        if request.user.is_authenticated:
            contact = Contact(user=request.user)
            print(contact)
            fm = ConttactForm(request.POST, instance=contact)

            if fm.is_valid():
                # name = fm.cleaned_data["name"]
                # email = fm.cleaned_data["email"]
                # contact = fm.cleaned_data["contact"]
                # query = fm.cleaned_data["query"]
                # message = f"Name :{name} Email:{email}, Contact:{contact} Message:{query}"
                # try:

                #     send_mail("heading", message, EMAIL_HOST_USER, [
                #               "Email where you want to get the message of user"])
                # except Exception as e:
                #     print(e)
                #     messages.error(
                #         request, "Something Error Occured. Please try later")

                fm.save()

                messages.success(request, "Your Query has been submitted")
                return redirect('/contact/')

    messages.warning(request, "You must have logged in")
    return render(request, 'blog/contact.html', {"form": fm})


def search(request):
    if request.method == "POST":
        text = request.POST.get("searchp")
        sresult = []
        allpost = Post.objects.all()
        for p in allpost:
            if (text in p.p_head1 or text in p.p_chead1 or text in p.p_head2 or text in p.p_chead2 or text in p.p_body or text in p.p_title):
                sresult.append(p)
        print(sresult)
        return render(request, 'blog/newblog.html', {"result": sresult, "search": True})
    
def postblog(request):
    fm=PostForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You must have logged in")
            return redirect("/")

        if request.user.is_authenticated:
            
            postuser = Post(p_author=request.user)
            fm = PostForm(request.POST, request.FILES, instance=postuser)
            print(request.FILES, request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Your Post has been succssfully posted")
                return redirect('/')
            # else:
            #     messages.error(request, "Invalid Post")
            #     return redirect('/')

    return render(request, 'blog/postblog.html', {"form": fm})

def mypost(request):
    allpost=Post.objects.filter(p_author=request.user)
    print(allpost)
    
    return render(request, "blog/mypost.html", {"all":allpost})