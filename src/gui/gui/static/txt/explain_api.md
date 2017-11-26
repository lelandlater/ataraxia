# Who uses the Cue API?

The Cue API is intended for use by software developers. Client applications interface with the Cue API at ```https://api.cue.zone/<version>/```. An access token is required in order to use the Cue API. Please visit the [main website](https://cue.zone).

**Python example**

```
$ python3.6
>>> import requests
>>> token = open('CueAPI_JWT.token').read()
>>> h = {'Authorization': f"Bearer {t}"}
>>> evid = open('event-id-from-ongoing-event.txt').read()
>>> a_day_on_the_couch = requests.get(f"https://api.cue.zone/v1/event/{evid}, headers=h)
...
```
