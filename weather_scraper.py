# weather_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    """
    http://quotes.toscrape.com/ から名言とその作者をスクレイピングして表示する関数
    """
    url = 'http://quotes.toscrape.com/'

    try:
        # Webサイトの情報を取得
        response = requests.get(url)
        response.raise_for_status() # HTTPエラーが発生した場合に例外を発生させる

        # 取得したHTMLをBeautifulSoupで解析
        soup = BeautifulSoup(response.text, 'html.parser')

        # 必要な情報（名言と作者）を探す
        # divタグでclassが'quote'の要素をすべて見つける
        quotes = soup.find_all('div', class_='quote')

        print(f"--- {url} からの名言 ---")
        if not quotes:
            print("名言が見つかりませんでした。")
        else:
            for quote in quotes:
                # 各quote要素の中から、名言のテキスト（spanタグでclass='text'）を取得
                text = quote.find('span', class_='text').get_text(strip=True)
                # 各quote要素の中から、作者の名前（smallタグでclass='author'）を取得
                author = quote.find('small', class_='author').get_text(strip=True)

                print(f"「{text}」 - {author}")
        print("--------------------------")

    except requests.exceptions.RequestException as e:
        print(f"Webサイトへのアクセスエラーが発生しました: {e}")
    except AttributeError: # find()でNoneが返ってきてget_text()を呼び出した場合など
        print("警告: ページ構造が予期しないものでした。要素が見つかりません。")
    except Exception as e:
        print(f"スクレイピング中に予期せぬエラーが発生しました: {e}")

# スクリプトが直接実行された場合に scrape_quotes 関数を呼び出す
if __name__ == "__main__":
    scrape_quotes()