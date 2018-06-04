import requests

my_data = { "firstname":"Mickey" ,"lastname":"Mouse" }
r = requests.post("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit/action_page.php", my_data)

f = open("myFile.html", "w+")
f.write(r.text)