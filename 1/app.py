from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-trained model and vectorizer
with open('ML/knn_model.pkl', 'rb') as model_file:
    knn_model = pickle.load(model_file)
    
with open('ML/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)
   
data = pd.read_csv('spotify_millsongdata.csv') 

app = Flask(__name__)

@app.route('/recommend', methods= ['POST'])
def recommend():
    user_input = request.json.get('lyrics', '')
    
    if not user_input:
        return jsonify({"error": "No lyrics provided"}), 400
    
    # Transform user input
    user_vector = vectorizer.transform([user_input])
    
    # Find recommendations 
    distances, indices = knn_model.kneighbors(user_vector)
    recommendations = data.iloc[indices[0]].to_dict(orient= 'records')
    
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)