import urllib.request
import json
import traceback

def post_json(url, data, output_file):
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type':'application/json'})
        response = urllib.request.urlopen(req, timeout=5)
        output_file.write(f"[{url}] SUCCESS: {response.status}\n")
        output_file.write(response.read().decode('utf-8') + "\n")
    except urllib.error.HTTPError as e:
        output_file.write(f"[{url}] HTTP ERROR: {e.code} {e.reason}\n")
        output_file.write(e.read().decode('utf-8', errors='replace') + "\n")
    except Exception as e:
        output_file.write(f"[{url}] ERROR: {e}\n")
        output_file.write(traceback.format_exc() + "\n")

with open('d:\\test_api_log.txt', 'w', encoding='utf-8') as f:
    post_json('http://127.0.0.1:5001/auth/admin/student/login', {'email':'test@example.com','password':'test'}, f)
    post_json('http://10.56.33.200:5001/auth/admin/student/login', {'email':'test@example.com','password':'test'}, f)
