import requests
f = requests.get('https://uselessfacts.jsph.pl/random.txt?language=en')

print(f.text)
print(f.text.split("\n")[0])