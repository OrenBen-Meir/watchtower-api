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

    def is_role_valid(self, role: str):
        valid_roles = [
            self.regular,
            self.reviewer,
            self.manager,
            self.admin
        ]
        return role in valid_roles


roles = Roles()
