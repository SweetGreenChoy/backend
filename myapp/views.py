from django.shortcuts import render, HttpResponse

# Create your views here.
def get_seats(request, seat):
	return HttpResponse("Seat reserved " + seat)

def ticket_reserve(request, seat):
	return HttpResponse("reserve web connect test "+ seat)

def ticket_index(request):
	return HttpResponse("index web connect test")

def get_seats(request):
	return HttpResponse("seat status")

def index_page(request):
	return render(request, 'myapp/index.html')