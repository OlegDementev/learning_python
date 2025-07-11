s = "orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley"

s_ = s.split()

res = {}

for i in s_:
    res[i] = res.get(i, 0) + 1

max_key = max(res.values())

n_res = {i: j for i, j in res.items() if j == max_key}

n_res__ = min(n_res)

print(n_res__)
