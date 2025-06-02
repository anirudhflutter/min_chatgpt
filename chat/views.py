from django.shortcuts import render
from django.http import JsonResponse
import openai

openai.api_key = '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'

def chat_page(request):
    return render(request, 'chat/index.html')

def ask_gpt(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response['choices'][0]['message']['content']
        return JsonResponse({'response': answer})
