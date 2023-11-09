import openai
from . import API_key
from django.shortcuts import render

openai.api_key = API_key.get_key()

def Chatbot(user_input):
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are witty british digital assistant, skilled in explaining complex health, finance and educational concepts whilest adding a hint of humour."},
        {"role": "user", "content": user_input}]
    )

    return respone.choices[0].message.content.strip("\n").strip(" ")

def Index(request):
    if request.method == "POST":
        user_input = request.POST["user_input"]

        chatbot = Chatbot(user_input)
        return render(request,"Index.html",{'chatbot':chatbot})
    
    else:
        return render(request, "Index.html")

