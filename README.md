# テーマインストール方法


1. ckanext-geoportal_themeを/usr/lib/ckan/default/src/ 以下に設置


2. . /usr/lib/ckan/default/bin/activate を実行


3. python /usr/lib/ckan/default/src/ckanext-geoportal_theme/setup.py develop を実行してインストール


4. /etc/ckan/default/production.ini を編集し、ckan.pluginsの末尾にgeoportal_themeを追記


5. Webサーバを再起動






# サイトロゴ、ファビコン、言語設定
1. CKAN iniファイルを開く


2. サイトロゴの設定（ロゴがある場所を指定）
         ckan.site_logo = /base/images/ckan-logo.png


3. faviconの設定
         ckan.favicon = /images/favicon.ico


4. デフォルト言語を日本語に設定
         ckan.locale_default = ja
         ckan.locale_order = ja
