import google.generativeai as genai

genai.configure(api_key="AIzaSyAaIBGH2kCerU7fALBHrhC9kPBZu-6Y01M")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

try:        
    convo = model.start_chat(history=[])
    convo.send_message("doha weather")
    print(convo.last.text)

except Exception as e:
    print("Something went wrong:", e)