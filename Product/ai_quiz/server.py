from flask import Flask, request, jsonify
from threading import Thread

app = Flask(__name__)

@app.route('/update_gaze', methods=['POST'])
def update_gaze():
    data = request.json
    # For example, store gaze data in session state
    # In a real scenario, you might process or store this data differently
    st.session_state["gaze_data"] = data
    return jsonify({"status": "success"}), 200

def run_flask():
    app.run(port=5000)

if __name__ == "__main__":
    Thread(target=run_flask).start()
