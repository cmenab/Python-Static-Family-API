
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers":[7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers":[10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers":[1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Recibe el body decodificado y le agrega el id y apellidos, luego lo agrega a la biblioteca correspondiente
        member["id"]=self._generateId()
        member["last_name"]=self.last_name
        self._members.append(member)
        return True

    def delete_member(self, id):
        # Recibe un id que corresponde a la posición en la biblioteca _members y a continuación lo borra
        self._members.pop(id)
        return True

        # Recibe un id que corresponde a la posición de la biblioteca y lo retorna
    def get_member(self, id):
        return self._members[id]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members