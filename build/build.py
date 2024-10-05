import os
import yaml
import json

contests = []

for contest in os.listdir("contests"):
    contest_name = contest.replace(".yaml", "").replace(".yml", "")
    with open(os.path.join("contests", contest), "r") as f:
        contest_obj = yaml.safe_load(f)
    contests.append(contest_obj)

def find_contests(problem_slug):
    ret = []
    for contest in contests:
        if problem_slug in contest["problems"]:
            ret.append(contest)
    assert len(ret) <= 1
    return ret[0] if ret else None

problem_documents = []

for problem in os.listdir("problems"):
    meta_path = os.path.join("problems", problem, "meta.yml")
    if os.path.exists(meta_path):
        with open(meta_path, "r") as f:
            meta_obj = yaml.safe_load(f)
        problem_documents.append({
            "title": meta_obj["title"],
            "tags": meta_obj["tags"],
            "slug": problem,
            "difficulty": meta_obj["difficulty"],
            "contest": find_contests(problem)["slug"]
        })

with open("build/index.html", "r") as f:
    base_index = f.read()

tags = set()
for problem in problem_documents:
    for tag in problem["tags"]:
        tags.add(tag)


base_index = base_index.replace("TEMPLATE_PROBLEMS", json.dumps(problem_documents))
base_index = base_index.replace("TEMPLATE_TAGS", json.dumps(list(tags)))
base_index = base_index.replace("TEMPLATE_CONTESTS", json.dumps([contest["slug"] for contest in contests]))

with open("docs/index.html", "w") as f:
    f.write(base_index)
