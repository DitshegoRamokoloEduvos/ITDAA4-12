{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "836673ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "from main import calculate_sum\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "import time\n",
    "\n",
    "\n",
    "def test_user_interface():\n",
    "    driver_path = r\"----------\\chromedriver.exe\"  # Path to chromedriver. Can end with .sh if on (Li/U)nix environments\n",
    "    options = Options()\n",
    "    options.add_argument(\"--headless\")  # To not open a real chrome window\n",
    "    with webdriver.Chrome(driver_path, chrome_options=options) as driver:\n",
    "        url = \"http://127.0.0.1:8501\"\n",
    "        driver.get(url)\n",
    "        time.sleep(5)\n",
    "        html = driver.page_source\n",
    "\n",
    "    assert \"Add numbers\" in html\n",
    "    assert \"First Number\" in html\n",
    "    assert \"Second Number\" in html\n",
    "\n",
    "\n",
    "def test_logic():\n",
    "    assert calculate_sum(1, 1) == 2\n",
    "    assert calculate_sum(1, -1) == 0\n",
    "    assert calculate_sum(1, 9) == 10\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    test_logic()\n",
    "    test_user_interface()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
