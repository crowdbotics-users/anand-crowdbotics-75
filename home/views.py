from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'admin-timeline', 'url': 'http://pypi.python.org/pypi/admin-timeline/0.5'},
    ]
    context = {
        'title': 'anand-crowdbotics-75',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
