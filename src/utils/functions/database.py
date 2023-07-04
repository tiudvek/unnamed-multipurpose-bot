class XataDBUtils:
    def __init__(self, client):
        self.client = client

    def new_user(self, userid: int, gayness: int):
        record = {"gayness": gayness}

        self.client.records().insertRecordWithID("users", str(userid), record)

    def check_exists(self, id: int):
        records = self.client.records()

        userQuery = records.getRecord("users", id)

        return False if userQuery.status_code == 404 else True
