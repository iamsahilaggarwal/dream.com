from django.http import HttpResponse
def home(request):
    return HttpResponse('''<H1>welcome</H1><br>
    <a href='/shop'>shop<a><br><br>
    <a href='/blog'>blog<a>''')