class Roles:

    @property
    def regular(self) -> str:
        return "regular"

    @property
    def reviewer(self) -> str:
        return "reviewer"

    @property
    def manager(self) -> str:
        return "manager"

    @property
    def admin(self) -> str:
        return "admin"

    def employees(self):
        return [
            self.reviewer,
            self.manager,
            self.admin
        ]

    def managers(self):
        return [
            self.manager,
            self.admin
        ]

    def all_roles(self):
        return [
            self.regular,
            self.reviewer,
            self.manager,
            self.admin
        ]

    def is_role_valid(self, role: str):
        return role in self.all_roles()


roles = Roles()
