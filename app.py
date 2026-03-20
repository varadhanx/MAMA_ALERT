from flask import Flask, request, jsonify

app = Flask(__name__)

def check_risk(bp, swelling, headache):
    if bp > 140 and (swelling == "yes" or headache == "yes"):
        return "EMERGENCY"
    elif bp > 130:
        return "MONITOR"
    else:
        return "SAFE"

@app.route('/')
def home():
    return "MamaAlert Maternal Triage System Running"

@app.route('/triage', methods=['POST'])
def triage():
    data = request.json
    
    bp = int(data.get("bp"))
    swelling = data.get("swelling")
    headache = data.get("headache")

    result = check_risk(bp, swelling, headache)

    return jsonify({
        "risk_level": result,
        "message": "Take immediate action" if result == "EMERGENCY" else "Regular monitoring"
    })

if __name__ == '__main__':
    app.run(debug=True)
