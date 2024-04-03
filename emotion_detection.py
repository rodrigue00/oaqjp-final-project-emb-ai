import json
import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'colere': None,
            'degout': None,
            'peur': None,
            'joie': None,
            'tristesse': None,
            'emotion_dominante': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()

    if response.status_code == 400:
        return {
            'colere': None,
            'degout': None,
            'peur': None,
            'joie': None,
            'tristesse': None,
            'emotion_dominante': None
        }

    emotions = response_json.get('emotionPredictions', [])
    if emotions:
        emotions = emotions[0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        return {
            'colere': emotions.get('anger', None),
            'degout': emotions.get('disgust', None),
            'peur': emotions.get('fear', None),
            'joie': emotions.get('joy', None),
            'tristesse': emotions.get('sadness', None),
            'emotion_dominante': dominant_emotion
        }
    else:
        return {
            'colere': None,
            'degout': None,
            'peur': None,
            'joie': None,
            'tristesse': None,
            'emotion_dominante': None
        }
