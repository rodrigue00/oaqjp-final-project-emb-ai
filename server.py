"""
Ce fichier contient le code pour le serveur de l'application d'analyse des émotions.
"""
from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Affiche la page d'accueil de l'application.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Analyse les émotions dans le texte fourni.
    """

    if request.method == 'POST':
        text_to_analyze = request.form['text']
    else:
        text_to_analyze = request.args.get('textToAnalyze', '')

    result = emotion_detector(text_to_analyze)
    if result['emotion_dominante'] is None:
        return "Texte invalide ! Veuillez réessayer!"

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
