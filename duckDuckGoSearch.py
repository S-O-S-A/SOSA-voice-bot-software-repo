import ddg3

r = ddg3.query("chief keef")

print(r.related[0].text)