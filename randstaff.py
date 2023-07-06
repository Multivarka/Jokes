import requests

class RandStuff:
    def __init__(self):
        self.api = "https://randstuff.ru"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"}

    def generate_random_joke(self):
        return requests.post(f"{self.api}/joke/generate", headers=self.headers).json()['joke']['text']