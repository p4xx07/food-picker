import requests
f = requests.get('https://uselessfacts.jsph.pl/random.txt?language=en')
text = f.text.split("\n")[0]
text = text.replace("> ", "")
print(text)