from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == "POST":
        names = request.POST['receivers_names'].split(',')[1:]
        adresses = request.POST['receivers_emails'].split(',')[1:]
        title = request.POST['title']
        body = request.POST['message']
        if body == "" or title == "":
            return render(request, "main/index.html", {"data": "error_title_body"})
        if len(adresses) == 0:
            return render(request, "main/index.html", {"data": "error_receivers"})
        for idx, adress in enumerate(adresses):
            new_body = body.replace("{name}", names[idx])
            new_title = title.replace("{name}", names[idx])
            send_mail(new_title, new_body, "codekoala7@gmail.com", [adress, ])
        return render(request, "main/index.html", {"data": "success"})

    else:
        return render(request, "main/index.html")
