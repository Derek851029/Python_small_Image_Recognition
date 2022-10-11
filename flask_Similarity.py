import requests
from flask import Flask, current_app, request, Response
from flask_cors import CORS
import json
import base64
import get_image_feature_vectors_app as image_to_npz
import cluster_image_feature_vectors_app as similarity

app = Flask(__name__)
CORS(app)

@app.route('/Similarity_comparison',methods=['POST'])
def Similarity_comparison():
    data = request.get_data()
    json_data = json.loads(data.decode("UTF-8"))
    app_image = json_data.get("Image")
    decode_img = base64.b64decode(app_image)

    save_app_path = 'C:/Users/Administrator/Desktop/app_image/'
    with open(''+save_app_path+'app_image.jpg','wb') as f:
        f.write(decode_img)

    image_to_npz.get_image_feature_vectors_app(save_app_path)
    most_similarity =  similarity.cluster(save_app_path)
    return_data = {'data':str(most_similarity)}

    return return_data
        

def app_run():
    app.run(host="192.168.2.81", port=5001)

if __name__ == "__main__":
    app_run() 