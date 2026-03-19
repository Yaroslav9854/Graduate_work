
def scroll_to_element(self, locator, attempts=5):
    self.global_timeout = 2
    element = None
    counter = 0
    while counter < attempts:
        self.driver.execute_script("window.scrollBy(0, 900);")
        sleep(1)
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            counter += 1
            continue
    return element