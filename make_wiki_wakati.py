import os
os.system('curl https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2 -o data/jawiki-latest-pages-articles.xml.bz2')
os.system('bzip2 -d data/jawiki-latest-pages-articles.xml.bz2')
os.system('apt-get install ruby2.3-dev')
os.system('sudo gem install wp2txt')
os.system('wp2txt --input-file data/jawiki-latest-pages-articles.xml')
os.system('cat data/jawiki-latest-pages-articles* > data/wiki.wp2txt')
os.system('mecab -b 100000 -Owakati data/wiki.wp2txt -o data/wiki_wakati.txt -d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd')