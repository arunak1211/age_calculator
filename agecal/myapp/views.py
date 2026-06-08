# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import date

def index(request):
    age = None
    if request.method == 'POST':
        birth_date_str = request.POST.get('birth_date')
        if birth_date_str:
            # Convert string from HTML input to date object
            birth_date = date.fromisoformat(birth_date_str)
            today = date.today()
            
            # The Logic: Subtract years, then adjust if birthday hasn't happened yet this year
            age = today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day)
            )

    return render(request, 'index.html', {'age': age})