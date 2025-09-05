import requests

#the required first parameter of the 'get' method is the 'url':
#x = requests.post('http://api.scraperapi.com?api_key=1e3669d66a1c6983f9d966a22140eff4&url=https://entries.horseracingnation.com/entries-results/aqueduct/2023-03-03')
x = requests.post('http://api.scraperapi.com?api_key=1e3669d66a1c6983f9d966a22140eff4&url=https://entries.horseracingnation.com/entries-results/belmont-park/2023-06-18')

#print the response text (the content of the requested file):
print(x.text)
