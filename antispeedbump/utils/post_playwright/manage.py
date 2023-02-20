import os
import re
import tempfile
import time
from typing import Optional, Union

from playwright.sync_api import sync_playwright, expect


class Post:
    DELAY = 100  # delay for simulating human entry

    def __init__(
            self,
            url: Optional[str] = "www.instagram.com",
            # username: str = "",
            # password: str = "",
            username: Optional[str] = "koddeneme260",
            password: Optional[str] = "uZZc4-YBY:5sVW?",
            # username: str = "bekocankod",
            # passwd: str = ")d3::b%&.X,u3^J",
            data_to_post: dict = {},
            headless: bool = False
            # driver_path: Optional[str] = os.path.join(
            #    os.getcwd(),
            #    f"antispeedbump/configs/driver/{platform.system().lower()}/chromedriver"
            # )
    ) -> None:
        self.username = username
        self.password = password
        self.data_to_post = data_to_post
        self.url = url
        self.downloadable = self.download()
        self.headless = headless

    def post(self) -> None:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=self.headless)
            context = browser.new_context()

            # Open new page
            self.page = context.new_page()

            # Go to https://www.instagram.com/
            self.page.goto("https://www.instagram.com/")

            # Click on Username field
            self.page.locator(
                "[aria-label=\"Phone number\\, username\\, or email\"]").click()

            # Fill with username
            self.page.locator("[aria-label=\"Phone number\\, username\\, or email\"]").type(self.username,
                                                                                            delay=self.DELAY)

            # Click on Password field
            self.page.locator("[aria-label=\"Password\"]").click()

            # Fill with password
            self.page.locator("[aria-label=\"Password\"]").type(self.password, delay=self.DELAY)

            # Click Log In
            self.page.locator("button:has-text(\"Log In\")").first.click()
            # page.wait_for_url("https://www.instagram.com/accounts/onetap/?next=%2F")

            # Click text=Not Now
            self.page.locator("text=Not Now").first.click()
            self.page.wait_for_url("https://www.instagram.com/")

            # Click text=Not Now
            self.page.locator("text=Not Now").first.click()

            # import time
            # time.sleep(10)

            # share button
            self.page.locator("//*[name()='svg' and @aria-label='New post']").click()

            # attach file
            expect(self.page).to_have_title(re.compile("Create new post"))

            # with self.page.expect_file_chooser() as fc:
            # b = self.page.get_by_role("button", name="Select from computer").click()
            dzs = self.page.locator(
                "//*[name()='svg' and @aria-label='Icon to represent media such as images or videos']")
            # self.drag_and_drop(
            #    buffer=self.data_to_post['binary_data'],
            #    drop_zone_selector=dzs)

            with self.page.expect_file_chooser() as fc:
                self.page.locator("button:has-text(\"Select from computer\"").click()
            fc.value.set_files(
                # self.downloadable['binary']
                files=[
                    {
                        "name": f"blob.{'mp4' if self.data_to_post['media']['is_video'] else 'jpeg'}",
                        "mimeType": 'video/mp4' if self.data_to_post['media']['is_video'] else 'image/jpeg',
                        "buffer": self.data_to_post['binary_data']
                    }
                ]
            )
            self.page.get_by_role("button", name="Next").click()
            self.page.get_by_role("button", name="Next").click()

            time.sleep(10)

    def drag_and_drop(self, buffer: bytes, drop_zone_selector) -> None:
        base64_post = base64.b64encode(buffer).decode("utf-8")

        # post_type = 'video/mp4' if self.data_to_post['media']['is_video'] else 'image/jpeg'
        is_video = self.data_to_post['media']['is_video']
        if is_video:
            os.chdir(tempfile.gettempdir())
            js_handler = """
                (data) => {
                    const dt = new DataTransfer();
                    // Convert the binary string to a hexadecimal string
                    const hexString = Uint8Array.from(atob(data), c => c.charCodeAt(0));
                    const file = new File([hexString], 'blob.jpeg', { type: 'image/jpeg' });
                    dt.items.add(file);
                    return dt;
                }
                """
        else:
            os.chdir(tempfile.gettempdir())
            js_handler = """
                (data) => {
                    const dt = new DataTransfer();
                    // Convert the binary string to a hexadecimal string
                    const hexString = Uint8Array.from(atob(data), c => c.charCodeAt(0));
                    const file = new File([hexString], 'blob.mp4', { type: 'video/mp4' });
                    dt.items.add(file);
                    return dt;
                }
                """

        # Create the DataTransfer and File
        data_transfer = self.page.evaluate_handle(js_handler, base64_post)
        # Dispatch the 'drop' event on the target element
        try:
            self.page.dispatch_event(drop_zone_selector, 'drop', {"dataTransfer": data_transfer.json_value()})
        except Exception as e:
            print(e)

        os.chdir(os.getcwd())

    def download(self) -> Union[dict, None]:
        media = self.data_to_post["media"]
        binary_data = self.data_to_post["binary_data"]
        is_video = media["is_video"]
        if is_video:
            filename = "blob.mp4"
        else:
            filename = "blob.jpeg"

        f = _download(blob=binary_data, filename=filename)

        return {
            "id": self.data_to_post['id'],
            "file_type": "video" if is_video else "image",
            "description": self.data_to_post["description"],
            "binary": f,
        }


def _download(blob, filename):
    import tempfile
    import os

    fp = os.path.join(tempfile.gettempdir(), filename)

    with open(fp, "wb") as f:
        f.write(blob)

    content_size = os.stat(fp).st_size
    if content_size <= 1024:
        print("content size is not bigger than 1024 mb")
        return None

    return fp


# p = Post().connect()

import base64
