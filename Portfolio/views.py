from django.shortcuts import render, redirect
from django.contrib import messages
from Portfolio.models import Contact, Internship
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# imports below is for sending mail
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
from django import template

# Create your views here.
@login_required(login_url="/auth/signin/")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/auth/signin/")
def contact(request):
    if request.method == "POST":
        get_name = request.POST.get("name")
        get_email = request.POST.get("email")
        get_phone = request.POST.get("number")
        get_dis = request.POST.get("description")
        check1 = Internship.objects.filter(email=get_email)
        if check1:
            messages.success(
                request,
                "You are Already submitted the Details, We willcontact you soon!..",
            )
            return redirect("/contact")
        query = Contact.objects.create(
            name=get_name, email=get_email, phonenumber=get_phone, description=get_dis
        )
        query.save()
        # email sending admin start from here
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_message = mail.EmailMessage(
            f"Email from: {get_name} ",
            f"User Email: {get_email}\nUser PhoneNumber: {get_phone}\n\n\nQuery: {get_dis}",
            from_email,
            ["hunter99802023@outlook.com"],
            connection=connection,
        )
        email_client = mail.EmailMessage(f"Murthy Response",
            f"Thanks for reaching us\n\nMurthy P G\n9980915515\nmurthy@gmail.com",
            from_email,[get_email],
            connection=connection,
        )
        connection.send_messages([email_message,email_client])
        connection.close()
      # ending of email sender
        messages.success(
            request, "Thanks for contacting! We will get back to you soon."
        )
        return redirect("/contact")

    return render(request, "contact.html")


@login_required(login_url="/auth/signin/")
def about(request):
    return render(request, "about.html")


@login_required(login_url="/auth/signin/")
def services(request):
    return render(request, "services.html")


@login_required(login_url="/auth/signin/")
def internshipdetails(request):
    return render(request, "internship.html")


@login_required(login_url="/auth/signin/")
def resume(request):
    return render(request, "resume.html")


@login_required(login_url="/auth/signin/")
def internshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request, "please login to access this page")
        return redirect("/auth/signin/")

    if request.method == "POST":
        get_fullname = request.POST.get("name")
        get_email = request.POST.get("email")
        get_usn = request.POST.get("usn")
        get_clg_name = request.POST.get("clg_name")
        get_start_date = request.POST.get("startdate")
        get_end_date = request.POST.get("enddate")
        get_offer = request.POST.get("offer")
        get_projreport = request.POST.get("projreport")
        # converting to upper case
        get_fullname = get_fullname.upper()
        get_usn = get_usn.upper()
        get_clg_name = get_clg_name.upper()
        get_projreport = get_projreport.upper()
        get_offer = get_offer.upper()

        check1 = Internship.objects.filter(usn=get_usn)
        check2 = Internship.objects.filter(email=get_email)
        if check1 or check2:
            messages.success(request, "You are Already submitted the Details!..")
            return redirect("/internshipdetails/")
        if request.user.username == get_email:
            query = Internship.objects.create(
                fullname=get_fullname,
                usn=get_usn,
                email=get_email,
                college_name=get_clg_name,
                offter_status=get_offer,
                start_date=get_start_date,
                end_date=get_end_date,
                proj_report=get_projreport,
            )
            query.save()
            messages.success(request, "Form is Submitted Successfully!..")
            return redirect("/internshipdetails/")
        else:
            messages.error(
                request,
                "Your email address is wrong, Please enetr correct email address!..",
            )
            return redirect("/internshipdetails/")

    return render(request, "internship.html")
