from helium import go_to, Button, wait_until

# read creds


def creds():
    import json
    with open('credientials.json') as f:
        cred = json.loads(f.read())
    return cred


def _login(self) -> bool:
    print("username in log: ", self.username)
    print("password in log: ", self.passwd)

    try:
        go_to(self.url)  # go to url
        # ***  LOGIN
        wait_until(Button("Log in").exists)  # wait for page fully loaded

        # find buttons
        username_button = self._find_attr("@username", with_s=True)[0]
        password_button = self._find_attr("@password", with_s=True)[0]
        login_button = self._find_attr(Button("Log in"))[0]

        #  interact
        self._fill(username_button, self.username)
        self._fill(password_button, self.passwd)
        self._button_event(attr=login_button)

        # *** Save Your Login Info?
        nn = Button("Not Now")
        wait_until(nn.exists)
        # find button
        not_now_button = self._find_attr(nn)[0]
        self._button_event(attr=not_now_button)

        # *** Turn on Notifications?
        nn = Button("Not Now")
        wait_until(nn.exists)
        # find button
        not_now_button = self._find_attr(nn)[0]
        self._button_event(attr=not_now_button)
        return True

    except Exception as e:
        print({f"_login_message": e})
        return False
