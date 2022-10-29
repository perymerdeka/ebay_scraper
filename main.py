
import requests
import pandas as pd

from bs4 import BeautifulSoup


url: str = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=computer+monitor&_sacat=0"

headers: dict = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def get_all_items() -> list:
    res = requests.get(url, headers=headers)
    print("process URL: {}".format(url))
    print("Status Code: {}".format(res.status_code))
    soup = BeautifulSoup(res.text, "html.parser")

    # scraping process

    products = soup.find("ul", attrs={"class": "srp-results srp-list clearfix"}).find_all("li", attrs={"class": "s-item"})
    products_list: list = []
    for product in products:
        link = product.find("a", attrs={"class": "s-item__link"})['href']
        title = product.find("span", attrs={"role": "heading"}).text.strip()
        
        # process data
        data_dict: dict = {
            "title": title,
            "link": link,
        }
        products_list.append(data_dict)
    

    # process data with pandas
    df = pd.DataFrame(products_list)
    df.to_csv("reports.csv", index=False)
    return "data generated"



if __name__ == "__main__":
    get_all_items()
