from django.shortcuts import render, redirect
from .models import Suggestion

def suggestion_view(request):
    if request.method == 'POST':
        suggestion_text = request.POST.get('suggestion')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        category = request.POST.get('category')
        rating = request.POST.get('rating')

          # Create a new Suggestion object and save it to the database
        suggestion = Suggestion(
            suggestion_text=suggestion_text,
            name=name,
            email=email,
            category=category,
            rating=rating
          )
        suggestion.save()

          # Redirect to a success page or render a success message
        return redirect('success')  # Replace 'success' with your success URL or view name

    return render(request, 'suggestion_form.html')  # Replace with your actual template name

def success_view(request):
    return render(request, 'success.html')