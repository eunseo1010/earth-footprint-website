"""Python standard-library web server. Run: python app.py"""
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
import json
ROOT = Path(__file__).resolve().parent
QUESTIONS = json.loads((ROOT / "questions.json").read_text(encoding="utf-8"))
PUBLIC = {"index.html", "style.css", "app.js", "questions.js", "assets/background.png", "assets/plant.png"}
def validate_answers(payload):
    if not isinstance(payload, dict) or set(payload) != {q["id"] for q in QUESTIONS}:
        raise ValueError("Exactly Q1 through Q7 are required.")
    cleaned = {}
    for question in QUESTIONS:
        value = payload[question["id"]]
        if not isinstance(value, str) or value not in [o["value"] for o in question["options"]]:
            raise ValueError("Invalid answer: " + question["id"])
        cleaned[question["id"]] = value
    return cleaned
class Handler(SimpleHTTPRequestHandler):
    def send_json(self, payload, status=200):
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/api/questions":
            return self.send_json(QUESTIONS)
        if path.lstrip("/") not in PUBLIC and path != "/":
            return self.send_error(404)
        return super().do_GET()
    def do_HEAD(self):
        path = self.path.split("?", 1)[0]
        if path.lstrip("/") not in PUBLIC and path != "/":
            return self.send_error(404)
        return super().do_HEAD()
    def do_POST(self):
        if self.path != "/api/answers":
            return self.send_error(404)
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= 16384:
                raise ValueError("Invalid request length")
            payload = json.loads(self.rfile.read(size).decode("utf-8"))
            answers = validate_answers(payload)
        except (ValueError, UnicodeError) as exc:
            return self.send_json({"ok": False, "error": str(exc)}, 400)
        # Integration point: pass answers to the team's carbon calculation function.
        # No emission factors are invented; no persistent server-side storage.
        return self.send_json({"ok": True, "answers": answers, "calculation_connected": False})
if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8000), partial(Handler, directory=str(ROOT)))
    print("Open http://127.0.0.1:8000 — Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
