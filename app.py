from flask import Flask, jsonify
import boto3

app = Flask(__name__)

@app.route("/files", methods=["GET"])
def fetch_file_list():
    try:
        s3 = boto3.client("s3")
        response = s3.list_objects(Bucket="redkube-bucket")
        files = [content["Key"] for content in response.get("Contents", [])]
        return jsonify(files)
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
