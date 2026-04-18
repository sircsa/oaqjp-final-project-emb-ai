import requests, json

# def emotion_detector(text_to_analyze):
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     myobject = {"raw_document": {"text": text_to_analyze}}
#     URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     response = requests.post(URL, json=myobject, headers=headers)
#     return response.json()

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=my_obj, headers=headers)
    
    # Check for success
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'label': dominant_emotion 
        }
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'label': None
        }
    
    return None