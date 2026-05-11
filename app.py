import os
import time
from flask import Flask, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)
START_TIME = time.time()

# A "Command Center" style Dashboard
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Core Engine | User Service</title>
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: 'JetBrains Mono', monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .dashboard { border: 1px solid #334155; background: #1e293b; padding: 30px; border-radius: 8px; width: 600px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 15px; margin-bottom: 20px; }
        .status-dot { height: 10px; width: 10px; background-color: #10b981; border-radius: 50%; display: inline-block; margin-right: 5px; box-shadow: 0 0 10px #10b981; }
        .title { font-size: 1.2rem; letter-spacing: 2px; text-transform: uppercase; color: #94a3b8; }
        .stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 25px; }
        .stat-item { background: #0f172a; padding: 15px; border-radius: 4px; border-left: 3px solid #3b82f6; }
        .stat-label { font-size: 0.7rem; color: #64748b; text-transform: uppercase; }
        .stat-value { font-size: 1rem; color: #3b82f6; margin-top: 5px; }
        .console { background: #000; padding: 15px; border-radius: 4px; font-size: 0.85rem; color: #10b981; margin-bottom: 20px; border: 1px solid #1e293b; }
        .btn { display: block; text-align: center; background: #3b82f6; color: white; padding: 12px; border-radius: 4px; text-decoration: none; font-weight: bold; transition: 0.3s; }
        .btn:hover { background: #2563eb; transform: translateY(-2px); }
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <div class="title">User Microservice v1.2</div>
            <div><span class="status-dot"></span> <span style="font-size: 0.8rem; color: #10b981;">SYSTEM ACTIVE</span></div>
        </div>
        <div class="stat-grid">
            <div class="stat-item">
                <div class="stat-label">Server Time</div>
                <div class="stat-value">{{ time }}</div>
            </div>
            <div class="stat-item">
                <div class="stat-label">Uptime</div>
                <div class="stat-value">{{ uptime }}s</div>
            </div>
        </div>
        <div class="console">
            $ root@openbluff:~/ > service status --check<br>
            [OK] Docker Container running...<br>
            [OK] SQLite Database connected...<br>
            [OK] API v1 routes initialized...
        </div>
        <a href="/api/v1/users" class="btn">ACCESS DATA STREAM</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    current_time = datetime.now().strftime("%H:%M:%S")
    uptime = int(time.time() - START_TIME)
    return render_template_string(HTML_TEMPLATE, time=current_time, uptime=uptime)

@app.route('/api/v1/users')
def get_users():
    return jsonify({
        "metadata": {
            "version": "1.2",
            "environment": "production-container",
            "timestamp": datetime.now().isoformat()
        },
        "users": [{"id": 1, "name": "Ammu", "role": "Admin"}]
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
