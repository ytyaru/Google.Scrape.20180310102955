#!/bin/bash
# 設定
user=ytyaru
desc="Google検索結果をスクレイピング"
url=http://ytyaru.hatenablog.com/entry/2019/02/09/000000
target=$(cd $(dirname $0) && pwd)

# Python環境準備
. ~/root/script/sh/pyenv.sh
. ~/root/env/py/auto_github/bin/activate

# 実行
#script=/media/mint/85f78c06-a96e-4020-ac36-9419b7e456db/mint/root/pj/auto/GitHub/python/v3.1/GitHubUploader.py
script=~/root/script/py/GitHub.Uploader.Pi3.Https.201802210700/src/Uploader.py
#script=/tmp/work/GitHub.Uploader.Pi3.Https.201802210700/src/Uploader.py
python3 ${script} "${target}" -u  "${user}" -d "${desc}" -l "${url}"

