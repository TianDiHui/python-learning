import requests
parmas = {"q":"doonabae"}

r = requests.get("http://www.bing.com/search",params=parmas)
print("status: ",r.status_code)
f = open("./page/page.html","w+")
f.write(r.text)
