import yaml

obj = {"test_cases": []}

def createBatch(batch: int, n: int, p: int):
    cur = {
        "batched" : [],
        "points" : p
    }
    for i in range(1,n + 1):
        cur["batched"].append({"in" : f"tests/{batch}_{i}.in","out":f"tests/{batch}_{i}.out"})

    obj["test_cases"].append(cur)

createBatch(0,1,0)
createBatch(1,10,100)
print(yaml.dump(obj,indent=2))
