# Python Webスクレイピングアプリ (名言抽出)

## 概要

このアプリは、Pythonを使用して特定のWebサイト (`http://quotes.toscrape.com/`) から情報を自動的に抽出するWebスクレイピングツールです。Webサイト上の名言とその作者を効率的に収集・表示することができます。

## 機能一覧

-   **Webページへのアクセス**: `http://quotes.toscrape.com/` に自動でアクセスし、HTMLコンテンツを取得します。
-   **HTML解析**: 取得したHTMLコードを解析し、構造化されたデータとして扱えるように準備します。
-   **特定情報の抽出**: ページ上のすべての名言（引用文）とその作者の名前を正確に探し出して抽出します。
-   **結果表示**: 抽出した名言と作者をターミナルに分かりやすく表示します。
-   **データ保存 (CSV形式)**: **抽出した名言と作者のデータを `quotes.csv` ファイルに保存します。このファイルはExcelなどの表計算ソフトで簡単に開くことができます。**
-   **エラーハンドリング**: Webサイトへのアクセス失敗や、予期しないページ構造の変更など、一般的なスクレイピング時のエラーに対応します。

## 使用技術

-   Python
-   `requests` ライブラリ (Webページ取得用)
-   `BeautifulSoup4` ライブラリ (HTML解析・情報抽出用)
-   `csv` ライブラリ (CSVファイル操作用)

## 使い方

1.  このリポジトリをあなたのPCにクローンします。
    ```bash
    git clone [https://github.com/hirose-prog/my-first-scraper.git](https://github.com/hirose-prog/my-first-scraper.git)
    ```
2.  プロジェクトのフォルダに移動します。
    ```bash
    cd my-first-scraper
    ```
3.  必要なライブラリをインストールします。
    ```bash
    pip install requests beautifulsoup4
    # または pip3 install requests beautifulsoup4
    ```
4.  アプリを起動します。
    ```bash
    python weather_scraper.py
    # または python3 weather_scraper.py
    ```
5.  ターミナルにスクレイピング結果（名言と作者）が表示され、`quotes.csv` ファイルが作成されます。

## このプロジェクトから学んだこと

このWebスクレイピングアプリの作成を通して、以下のプログラミングとデータ収集の基礎を実践的に習得しました。

-   Pythonの応用文法（関数、ループ、条件分岐、データ構造）
-   `requests` ライブラリを使ったWebページへのアクセスとデータ取得
-   `BeautifulSoup4` ライブラリを使ったHTMLの解析と、特定の情報（タグ、クラス）の抽出方法
-   **`csv` ライブラリを使ったCSVファイルの読み書きとデータ保存**
-   Webスクレイピングにおけるエラーハンドリング（ネットワークエラー、ページ構造の変更への対応）
-   **実践的な情報収集自動化スクリプトの開発経験**
-   **GitとGitHubの高度なワークフロー**:
    -   リポジトリの作成と初期化
    -   ファイルの追加とコミット（`git add`, `git commit`）
    -   リモートリポジトリの設定と管理（`git remote add`）
    -   GitHubへのコードのプッシュ（`git push`）
    -   リモートの変更を取り込むプル（`git pull`、**特に履歴の分岐解決（`--allow-unrelated-histories`）や複雑なマージコンフリクトの解決**）
    -   Personal Access Token（PAT）を使用した認証方法

---
