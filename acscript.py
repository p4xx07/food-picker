import requests

headers = {
#':authority': 'api.turnip.exchange',
#':method': 'GET',
#':path': '/islands/',
#':scheme': 'https',
'accept': 'application/json',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
'content-type': 'application/json',
'origin': 'https://turnip.exchange',
'referer': 'https://turnip.exchange/islands',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97',
'x-kpsdk-ct': 'o72kIUn1e4q+vbMlpjFKuA==::tfiWy/5f9OZWnbmTdSGIczZDpc4G/wurlRXuA/4cTpn9LrDp2dIRQrBEzmZpnX6QTCDE9EnTh7vAVWirGPzU47D8A72+br7SS4xOBaBDJxgxnGam8Cc4rbeB0ZKpg6nfTueUXVRzMTkS+pwMa7yyAQlRv7OcoGOjSxSSJPIuWQMqrlHH6FbeBzHEIqC5qwesAlJjMJeBsSm6cXMfOpM65EGPC4UN2WRrVz60fPTkTW7AHiQTMvPCES6rfFpowLT32mL0EIlS2H5Mg6W/QnthbzIyQr37DUwbgQH6HFKVhgFKucPJCy6HdaaN1nr3inFvG1E4jZwcxR5pPz1Tej4nH7fpnbS9OQYyOQvBuGi7ifDbcTMxtCS9HWev8CHN2v2OKPH9l59N+6b6t4MB5NOeS1xDdfXwuU6M6u0DZmoWsjwLKNmkI1no0ok9yGYeHvPIFY5a+paAdyKEA8Z5YScJ8Xzq+aoh4NHNL6Dd9audCO/+axIAPE8XaB6iJlj3NdHPActO/phyD+IUnBPDkJ1WaRZZK5OYzUxx5+eBrsjYpWE=',
'x-kpsdk-fp': 'eb313b5c-f497-68c1-a0a7-c0573b871019'
}


r = requests.get('https://api.turnip.exchange/islands', headers=headers).json()
print(str(r))
print(r)

