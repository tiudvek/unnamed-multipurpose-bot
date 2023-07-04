class XataDBUtils:
    def __init__(self, client):
        self.client = client

    def new_user(self, userid: int, gayness: int):
        record = {"user_id": userid, "gayness": gayness}

        self.client.records().insertRecord("users", record)
