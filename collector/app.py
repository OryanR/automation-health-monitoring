from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Temporary in-memory storage before we add MySQL
data_log = []


@app.route('/report', methods=['POST'])
def receive_report():
    report = request.get_json()
    report['received_at'] = datetime.datetime.now().isoformat()

    # Logic to handle critical alerts
    if report.get('status') == 'CRITICAL':
        print(f"!!! ALERT: {report['hostname']} reporting CRITICAL status !!!")

    data_log.append(report)
    print(f"Received health report from {report['hostname']} ({report['os']})")

    return jsonify({"message": "Data received successfully"}), 201


if __name__ == '__main__':
    # Running on 0.0.0.0 so it is accessible within the Docker network
    app.run(host='0.0.0.0', port=5000)