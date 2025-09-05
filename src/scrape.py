import requests
import json
import time


def getJobResultBody(resultUrl):
  bodyHtml = None
  jobResult = None
  iteration = 1
  abort = False
  
  while (jobResult is None):
    time.sleep(10)
    print(f'{iteration}:Getting jobResult from: {resultUrl}')
    # post the statusUrl to get the content response
    res = requests.get(resultUrl)
    print(f'res.status_code: {res.status_code}')
    jobResult = json.loads(res.content)
    if(jobResult['status'] == 'finished'):
      print(f'jobResult returned: {jobResult["status"]}')
      body = jobResult['response']['body']
      bodyHtml = body.replace('\n','')
    else:
      print(f'jobResult status is : {jobResult["status"]}')
      jobResult = None
      iteration += 1
      if(iteration == 5):
        print(f'Break out of getJobResultBody() while loop')
        break
  
  return bodyHtml


scraperApi = 'https://async.scraperapi.com/jobs'
apiKey = '1e3669d66a1c6983f9d966a22140eff4'
belmont = 'https://entries.horseracingnation.com/entries-results/belmont-park/2023-06-18'
#sa = 'https://entries.horseracingnation.com/entries-results/santa-anita/2023-06-18'
sa = 'https://entries.horseracingnation.com/entries-results/2025-08-02'

# Set the race Result page to fetch
resultUrl = sa
jsonObj = {'apiKey': apiKey, 
           'url': resultUrl}
#jsonStr = json.dumps(jsonObj)

r = requests.post(url = scraperApi, 
                  json = jsonObj
                )

print(f'response =\n {r}')
print(f'response =\n {r.content}')

res = json.loads(r.text)
print(f'request returned: {res["status"]}')

raceResultsHtml = None
if(res['status'] == "running") :
  print(f'Screen scraper is running!')
  raceResultsHtml = getJobResultBody(res['statusUrl'])
  if (raceResultsHtml):
    print(f'Race Results Returned!')
  else:
    print(f'No Race Results HTML Returned!')
else:
  if(res['status'] == "finished"):
    print(f'request returned: {res["status"]}')
    raceResultsHtml = res['body'].replace('\n','')
    f = open("santa-anita-results.txt", "w")
    f.write(raceResultsHtml)
    print(f'HTML Written to file and closed {f.name}')
    f.close()
  else:
    print(f'Screen scraper returned with: {res.status}')

  
#print the response text (the content of the requested file):
print(f'RaceResultsHtml: processed!')


