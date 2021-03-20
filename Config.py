import json
import os

class JSON():

    #data = {}
    name = None

    def __init__(self, name, default):
        if not os.path.exists(f"{name}.json"):
            f = open(f"{name}.json", "w+")
            f.write(json.dumps(default))
            f.close

        self.name = f"{name}.json"

        f = open(f"{name}.json", "r+")
        json.loads(f.read())
        f.close()

    def setPollResultForUser(self, user, points):
        f = open(self.name, "r+")
        j = json.loads(f.read())
        f.close()
        j["quiz"].update({user: points})
        with open(self.name, 'w') as json_file:
            json.dump(j, json_file)
            json_file.close()

    def addPollResultForUser(self, user, points):
        f = open(self.name, "r+")
        j = json.loads(f.read())
        f.close()
        points = j["quiz"][user]
        points = points + 1

        j["quiz"].update({user: points})
        print(j)

        with open(self.name, 'w') as json_file:
            json.dump(j, json_file)
            json_file.close()

    def getList(self, key):
        f = open(self.name, "r+")
        j = json.loads(f.read())
        f.close()

        return j[key]


    def appendList(self, key, value):
        f = open(self.name, "r+")
        j = json.loads(f.read())
        f.close()

        j[key].append(value)

        with open(self.name, 'w') as json_file:
            json.dump(j, json_file)
            json_file.close()

    def removeDSGVO(self, user):
        f = open(self.name, "r+")
        j = json.loads(f.read())
        f.close()

        j["dsgvo"].remove(user)
        del j["quiz"][user]

        with open(self.name, 'w') as json_file:
            json.dump(j, json_file)
            json_file.close()


