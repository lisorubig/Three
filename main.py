class TreeStore:
    def __init__(self, lists: list):
        self.lists = lists
        self.dicts = self._to_dicts(self.lists)

    def _to_dicts(self, lists: list) -> dict:
        return {i['id']: i for i in lists}

    def getAll(self) -> list:
        return self.lists

    def getItem(self, dict_id: int) -> dict:
        return self.dicts.get(dict_id, {})

    def getChildren(self, dict_id: int) -> list:
        return [v for v in self.dicts.values() if v["parent"] == dict_id]

    def getAllParents(self, dict_id: int) -> list:
        return_list = []
        while True:
            for k, v in self.dicts.items():
                if k == dict_id:
                    return_list.append(v)
                    dict_id = v["parent"]
                    break

            if dict_id == 'root':
                return return_list


if __name__ == "__main__":
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"}, {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"}, {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}
    ]

    z = TreeStore(items)

    print(z.getChildren(4))
