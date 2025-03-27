from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import speak  # Import the speak function from utils.py
import threading
import pyttsx3

from django.shortcuts import render
from .models import PlayerScore

@csrf_exempt  # Disable CSRF for testing (optional, use CSRF token in production)



def do_voices(request):
    if request.method == "POST":
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            text = data.get("text", "No input text received")

            if not text.strip():
                return JsonResponse({"error": "Empty text received"}, status=400)

            def run_tts():
                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()

            # Run text-to-speech in a separate thread
            tts_thread = threading.Thread(target=run_tts)
            tts_thread.start()

            return JsonResponse({"message": f"Speaking: {text}"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON received"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    # Return error for any other method (e.g., GET)
    return JsonResponse({"error": "Invalid request method"}, status=405)


from django.http import JsonResponse
from .models import PlayerScore
import json

@csrf_exempt # thisis not supposed ot be here when not testing
# This view will receive data from the frontend (name, moves, time) and save it to the database.
def save_score(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            moves = data.get("moves")
            time_elapsed = data.get("time_elapsed")

            if not name or moves is None or time_elapsed is None:
                return JsonResponse({"error": "Missing data"}, status=400)

            # Save to database
            PlayerScore.objects.create(name=name, moves=moves, time_elapsed=time_elapsed)
            
            return JsonResponse({"message": "Score saved successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

 #This is for viewing the leaderboard
 

def leaderboard(request):
    scores = PlayerScore.objects.order_by("moves", "time_elapsed")[:10]  # Top 10 scores
    return render(request, "leaderboard.html", {"scores": scores})

# Create your views here.
def game1(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def start(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

