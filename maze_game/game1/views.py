from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import speak  # Import the speak function from utils.py

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


# Create your views here.
def game1(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def start(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
