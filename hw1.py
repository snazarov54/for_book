def create_dict(lines, d={}):
    text = []
    s = ""
    for line in lines:
        s += ' ' + line
    
    text = s.split()
    op = {text[i]: i for i in range(len(text))}
d1 = create_dict(["Cho, kak"])d1 = create_dict(["Cho, kak"])


    if d == {}:
        d.clear()
    d.update(op)
    return d

d1 = create_dict(["Cho, kak"])
print(d1)

d2 = create_dict(["Cho , kak", "normalno a ti Cho"], d1)
print(d2)
print(d2 is d1)
print(create_dict(["tut net takih slov"]))