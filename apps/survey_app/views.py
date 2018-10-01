from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):

    # request.session.clear()

    if "name" not in request.session:
        request.session["name"] = ""
    if "language" not in request.session:
        request.session["language"] = ""
    if "location" not in request.session:
        request.session["location"] = ""
    if "comment" not in request.session:
        request.session["comment"] = ""

    return render(request, "survey_app/index.html")

def process(request):
    # print("I am process")
    # print(request.POST)
    # print(request.POST["Location"])

    errors = []

    if(not request.POST["name"]):
        errors.append("Name Required")
        # print("name not given")

    if(not request.POST["language"]):
        errors.append("Language Required")

    if(not request.POST["location"]):
        errors.append("Location Required")

    request.session["form_data"] = request.POST

    if(errors):
        for error_message in errors:
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")

    return(redirect("/results"))

def results(request):
    # flash("You have completed this survey.")
    messages.add_message(request, messages.SUCCESS, 'Survey Complete.', fail_silently = True)
    return(render(request, "survey_app/results.html"))

def back(request):
    request.session.clear()
    return redirect("/")
