# Import the requests library to handle HTTP requests
import requests
import json  

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):  

    # URL of the emotion_detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } } 

    # Set the headers required for the API request 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)  
    
    
    #If status_code == 400, return all None values
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    
    # Convert returned JSON text to dictionary
    response_dict = json.loads(response.text)

    # Extract emotion scores from your response structure
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    # Pull required emotions
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    #get the dominant emotion
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy":joy_score,
        "sadness": sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    #return expected output
    return {
        
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }
