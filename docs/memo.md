# Google Scraping

検索結果ページのHTMLソースコードを目視で解析。

`id=main`要素内がメインコンテンツ。

* `<div class="rc">`で1件あたりの検索結果？
    * なぜか`soup.select('.rc')`できなかった
        * `'.g'`で成功

