import json
import jsonschema
from jsonschema import validate
import unicodedata


MySchema = {
    "type": "object",
    "properties": {
        "subreddit": {"type": "string"},
        "title": {"type": "string"},
        "selftext": {"type": "string"},
        "upvote_ratio": {"type": "number", "minimum": 0},
        "ups": {"type": "number", "minimum": 0},
        "downs": {"type": "number", "minimum": 0},
        "score": {"type": "number", "minimum": 0},
    },
}

sanitizedJson = []
errors = []


def ignoreUnicodeStr(s):
    return unicodedata.normalize('NFD', s)


def loadJsonFile(filename):
    with open(filename) as file:
        data = json.load(file)
        # for i in data:
        #     sanitizedJson.append({ignoreUnicodeStr(i["subreddit"]), ignoreUnicodeStr(i["title"]), ignoreUnicodeStr(i["selftext"]), i["upvote_ratio"], i["ups"], i["downs"], i["score"]})
        # print(sanitizedJson)
        return data


exampleJsonData = loadJsonFile("out.json")


#
# sanitizedJson = ignoreUnicodeStr(exampleJsonData)


def validateJson(jsonData):
    try:
        for f in jsonData:
            validate(instance=f, schema=MySchema)
    except jsonschema.exceptions.ValidationError as err:
        errors.append(err)
        return False
    return True


print(validateJson(exampleJsonData))