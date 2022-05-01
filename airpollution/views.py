from django.shortcuts import render


def welcome(request):
    context = {
        'app_name': request.resolver_match.app_name
    }
    return render(request, 'airpollution/welcome.html', context)


def upload_file(request):
    context = {
        'app_name': request.resolver_match.app_name,
        'message_success': 'The file has been uploaded successfully!'
    }
    return render(request, 'airpollution/welcome.html')
