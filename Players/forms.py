from django import forms

class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)

# import requests, uuid, json

# # Add your subscription key and endpoint
# subscription_key = "aeae4eb5841c44bbb965a93fa6bda34a"
# endpoint = "https://api.cognitive.microsofttranslator.com"

# # Add your location, also known as region. The default is global.
# # This is required if using a Cognitive Services resource.
# location = "global"

# path = '/translate'
# constructed_url = endpoint + path

# params = {
#     'api-version': '3.0',
#     'from': 'en',
#     'to': ['fr', 'it']
# }
# constructed_url = endpoint + path

# headers = {
#     'Ocp-Apim-Subscription-Key': subscription_key,
#     'Ocp-Apim-Subscription-Region': location,
#     'Content-type': 'application/json',
#     'X-ClientTraceId': str(uuid.uuid4())
# }

# # You can pass more than one object in body.
# body = [{
#     'text': 'Hello'
# }]

# request = requests.post(constructed_url, params=params, headers=headers, json=body)
# response = request.json()

# print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))