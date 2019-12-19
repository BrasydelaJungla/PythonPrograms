
#!/usr/bin/python3

thisdict = {
	"brand":"Ford",
	"model" : "Mustang",
	"year"  : "1964"
}

x = thisdict.get("model")

print(thisdict)

print(x)

thisdict["brand"]="BMW"

y = thisdict.get("brand")

print(y)


