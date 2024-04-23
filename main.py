import openai
import time
import serial
import speech_recognition as sr

#openai.api_key = "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"

ser = serial.Serial('COM14', 9600)
recognizer = sr.Recognizer()


def turnOnMicrowave():
    ser.write(b'1')
    print("Microwave is turned on.")


def turnOnLivingRoom():
    ser.write(b'2')
    print("Living Room is light turned on.")


def turnOnKitchen():
    ser.write(b'3')
    print("Kitchen is lights turned on.")


def turnOnFan():
    ser.write(b'4')
    print("Fan is turned on.")


def turnOnTv():
    ser.write(b'5')
    print("Tv is turned on.")


def receiveSignal():
    time.sleep(15)
    return True


def notifyUser():
    print("Done!")


def recognize_speech():
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


def run_conversation():
    user_input = recognize_speech()

    if user_input:
        print(f"User said: {user_input}")
        messages = [{"role": "user", "content": user_input}]
        functions = [
            {
                "name": "turnOnMicrowave",
                "description": "turn Microwave on, and if the user is hungry, i want to eat",
                "parameters": {"type": "object", "properties": {}},
            },
            {
                "name": "turnOnLivingRoom",
                "description": "Turn Living Room light on, and  if the user wants to chill, i,m tired ",
                "parameters": {"type": "object", "properties": {}},
            },
            {
                "name": "turnOnKitchen",
                "description": "turn on kitchen lights, and if the user wants to cook,i want to cook",
                "parameters": {"type": "object", "properties": {}},
            },
            {
                "name": "turnOnFan",
                "description": "turn fan on, and if the user is feeling hot, im feeling hot",
                "parameters": {"type": "object", "properties": {}},
            },
            {
                "name": "turnOnTv",
                "description": "turn on the tv, i want to watch a movie or a series, i want to watch the football game",
                "parameters": {"type": "object", "properties": {}},
            },
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=functions,
            function_call="auto"
        )

        response_message = response["choices"][0]["message"]
        print(response_message)

        if response_message.get("function_call"):
            available_functions = {
                "turnOnMicrowave": turnOnMicrowave,
                "turnOnLivingRoom": turnOnLivingRoom,
                "turnOnFan": turnOnFan,
                "turnOnKitchen": turnOnKitchen,
                "turnOnTv": turnOnTv,
            }
            function_name = response_message["function_call"]["name"]

            if function_name in available_functions:
                function_to_call = available_functions[function_name]
                function_to_call()

                if receiveSignal():
                    notifyUser()


run_conversation()

time.sleep(3)

while True:
    pass
