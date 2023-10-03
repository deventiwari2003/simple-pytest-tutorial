import requests
class Numx:
    def __init__(self, number):
        self.number = number

    def get_fact(self):
        #print(self.number)
        url = f"http://numbersapi.com/{self.number}"
        r = requests.get(url)
        if r.status_code == 200:
            print(r.text)
        else:
            print(f"Error occurred code ={r.status_code}")