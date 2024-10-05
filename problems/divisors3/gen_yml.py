import os
import yaml

test_names = [
    (name, name.split(".")[0].split("_")[0])
    for name in os.listdir(os.path.join(os.path.dirname(__file__), "tests"))
    if name.endswith(".in")
]

batches = {
    batch: [name for (name, b) in test_names if b == batch]
    for batch in set(tup[1] for tup in test_names)
}

def make_test(name):
    return {
        "in": f"tests/{name}",
        "out": f"tests/{name.replace('.in', '.out')}"
    }


cases = []
cases.append({
    "points": 100,
    "batched": [make_test(name) for name in batches["1"]]
})

obj = {
    "test_cases": cases,
    "checker": "checker.py"
}


print(yaml.safe_dump(obj, indent=2))
