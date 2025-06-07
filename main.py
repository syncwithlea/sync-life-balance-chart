from flask import Flask, request, send_file
from chart import generate_chart

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "SYNC Life Balance Chart API is running."

@app.route("/chart", methods=["POST"])
def chart():
    data = request.json
    try:
        category_score_map = {}

        for k, v in data.items():
            # Skip metadata fields like "Submitted at"
            if not isinstance(v, (int, float, str)):
                continue

            # Only process values that are probably numeric
            try:
                score = float(v)
            except:
                continue

            # Remove number prefix like "1. "
            cleaned_key = k.strip()
            if ". " in cleaned_key:
                cleaned_key = cleaned_key.split(". ", 1)[1]
            elif "." in cleaned_key:
                cleaned_key = cleaned_key.split(".", 1)[1]

            # Split before "How" if it exists
            if "How" in cleaned_key:
                category = cleaned_key.split("How", 1)[0].strip()
            else:
                category = cleaned_key.strip()

            category_score_map[category.upper()] = score

        scores = list(category_score_map.values())
        categories = list(category_score_map.keys())

        path = generate_chart(scores, categories)
        return send_file(path, mimetype='image/png')

    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
