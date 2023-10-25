from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Milestone

def index_view(request):
    return render(request, 'index.html')

@login_required
def journey_view(request):
    user = request.user  # Get the current logged-in user
    
    # Query the Milestone model to get user-specific data
    user_milestones = Milestone.objects.filter(user=user)
    
    context = {
        'user_milestones': user_milestones,  # Pass the data to the template
    }
    return render(request, 'journey.html', context)