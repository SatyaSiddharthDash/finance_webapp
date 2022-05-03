from django.shortcuts import render
from django import forms


class ExcelUploadForm(forms.Form):
    year = forms.CharField(max_length=4)
    file = forms.FileField()


def welcome(request):
    context = {
        'app_name': request.resolver_match.app_name
    }
    return render(request, 'airpollution/welcome.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']  # this is the name of the form tag in the html template
    else:
        pass

    context = {
        'app_name': request.resolver_match.app_name,
        'message_success': 'The file has been uploaded successfully!'
    }
    return render(request, 'airpollution/welcome.html')
