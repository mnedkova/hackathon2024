from flask import Flask, request, jsonify, render_template
from Aidanscrapestore import menu_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_food():
    food_name = request.args.get('foodName','').lower()
    if not food_name:
        return jsonify({"error": "No food name provided"}), 400

    results = []
    # Perform the search
    for key, data in menu_data.items():
        date = data["date"]
        location = data["location"]
        
        for item in data["meals"]:
            if food_name in item["food"].lower():
                results.append({
                    "meal": item["meal"],
                    "food": item["food"],
                    "location": location,
                    "date": date
                })
    # Return the results or a message if not found
    return jsonify(results if results else {"message": "No matches found"}), 200 if results else 404

if __name__ == "__main__":
    app.run(debug=True)
