class _CookieNames:

    @property
    def session(self) -> str:
        return "JSESSIONID"


cookie_names = _CookieNames()
