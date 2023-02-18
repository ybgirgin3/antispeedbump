import time

from helium import Button, wait_until, drag_file, Text

from .login import _login


def _post(self) -> bool:
    print("api url: ", self.url)
    try:
        # *** LOGIN
        _login(self)

        # *** share
        share_button = self._find_attr(
            "//*[name()='svg' and @aria-label='New post']",
            with_s=True,
            prefix="share button",
        )[0]
        # find button
        wait_until(share_button.exists)
        self._button_event(attr=share_button)

        # attach file
        drag_file(self.downloadable["binary"],
                  to="Drag photos and videos here")

        # is_video?
        if self.downloadable["file_type"] == "video":
            ok = Button("OK")
            wait_until(ok.exists)
            self._button_event(attr=ok)

        # *** Aspect Ration
        # crop button
        crop_button = self._find_attr(
            "//*[name()='svg' and @aria-label='Select crop']",
            with_s=True,
            prefix="crop button",
        )[0]
        wait_until(crop_button.exists)
        self._button_event(attr=crop_button)

        # original button
        org = Button("Original")
        wait_until(org.exists)
        self._button_event(attr=org)

        # next session (two times in a row)
        # first
        ns = Button("Next")
        wait_until(ns.exists)
        self._button_event(attr=ns)

        time.sleep(3)

        # second
        ns = Button("Next")
        wait_until(ns.exists)
        self._button_event(attr=ns)

        # *** Write a Description
        # find description area
        time.sleep(3)
        desc_area = self._find_attr(
            #attr="//*[name()='textarea' and @aria-label='Write a caption...']",
            attr="//html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea",
            with_s=True,
            prefix="desc area",
        )[0]
        wait_until(desc_area.exists)

        self._fill(
            attr=desc_area,
            value=f"({self.downloadable['id']}) {self.downloadable['description']}"
        )

        # Share post
        sb = Button("Share")
        wait_until(sb.exists)
        self._button_event(attr=sb)

        # Wait for the "Your post has beed shared" message
        # time.sleep(5)

        # cs = Text("Your post could not be shared. Please try again.")
        ps = Text("Your post has been shared.")
        time.sleep(15)

        # TODO: Post yollarken eğer try again çıkarsa ve o butona basarsak,
        # post yollanma işlemi aynı ayarlar ile tekrardan devam ediyor ve genellikle
        # yollama işlemi başarılı oluyor.
        # eğer try again gelirse o butona bastır...

        ret: bool = False

        if ps.exists:
            print("Your post has been shared.")
            ret = True

        else:
            print("Your post could not be shared. Please try again.")
            ret = False

        self._driver.quit()
        return ret

    except Exception as e:
        print("Error while posting content: ", e)
        return False
