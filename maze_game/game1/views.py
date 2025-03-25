from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import speak  # Import the speak function from utils.py


from django.shortcuts import render
from .models import PlayerScore

@csrf_exempt  # Disable CSRF for testing (optional, use CSRF token in production)
def do_voices(request):
    if request.method == 'POST':  # Handle only POST requests
        print("Received a POST request")  # Debugging line
        try:
            # Get JSON data from frontend
            data = json.loads(request.body)  
            command = data.get('command', '')
            print(f"Command: {command}")  # Check the received command

            # Process the command (Customize this for your game logic)
            if command:
                response = f'Processing your command: {command}'
                # Speak the response (server-side TTS)
                speak(response)  # Calls the speak() function in utils.py

                return JsonResponse({"message": response})
            else:
                return JsonResponse({"error": "No command received"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    
    # Return error for any other method (e.g., GET)
    return JsonResponse({"error": "Invalid request method"}, status=405)


from django.http import JsonResponse
from .models import PlayerScore
import json

@csrf_exempt
# This view will receive data from the frontend (name, moves, time) and save it to the database.
def save_score(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            name = data.get('name', '')
            moves = data.get('moves', 0)
            time_elapsed = data.get('time_elapsed', 0.0)

            if not name:
                return JsonResponse({"error": "Player name is required"}, status=400)

            # Save to the database
            player_score = PlayerScore.objects.create(
                name=name,
                moves=moves,
                time_elapsed=time_elapsed
            )

            # Return a success response
            return JsonResponse({"message": "Score saved successfully!"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
 #This is for viewing the leaderboard
 

def leaderboard(request):
    # Fetch all scores, ordered by time_elapsed or moves, depending on your game logic
    scores = PlayerScore.objects.all().order_by('time_elapsed')  # You can change ordering here
    return render(request, 'leaderboard.html', {'scores': scores})

# Create your views here.
def game1(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def start(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

