import feedparser
import tldextract
from datetime import datetime

def pubdate_dateonly(full_pubdate):
   return ' '.join(list(full_pubdate.split(" "))[1:4])
    
def today_dateonly(output_format='%d %b %Y'):
   str_today = ''.join(list(str(datetime.utcnow()).split(" "))[0])
   date = datetime.strptime(str_today, "%Y-%m-%d")
   #return datetime.strftime(date, "%d %b %Y")
   return datetime.strftime(date, output_format)

def get_source(domain):
    ext=tldextract.extract(domain)
    #return ext.subdomain + '.' + ext.domain + '.' + ext.suffix
    return ext.domain + '.' + ext.suffix

def is_published_today(full_pubdate):
    retval=False

    if today_dateonly() == pubdate_dateonly(full_pubdate):
        retval=True

    return retval

crypto_feedlist=[
                 'https://decrypt.co/feed', 
                 'https://www.coindesk.com/arc/outboundfeeds/rss/?outputType=xml', 
                 'https://cointelegraph.com/rss/tag/altcoin',
                 'https://cointelegraph.com/rss/tag/bitcoin',
                 'https://cointelegraph.com/rss/tag/blockchain',
                 'https://cointelegraph.com/rss/tag/ethereum',
                 'https://cointelegraph.com/rss/tag/litecoin',
                 'https://cointelegraph.com/rss/tag/regulation',
                 'https://bitcoinmagazine.com/.rss/full/',
                 'https://cryptopotato.com/feed/',
                 'https://cryptocurrencynews.com/technology/feed/',
                 'https://cryptocurrencynews.com/business/feed/',
                 'https://cryptocurrencynews.com/daily-news/ethereum-news/feed/',
                 'https://cryptocurrencynews.com/daily-news/bitcoin-news/feed/',
                 'https://cryptocurrencynews.com/daily-news/crypto-news/feed/',
                 'https://cryptocurrencynews.com/icos/ico-news/feed/',
                 'https://cryptocurrencynews.com/info/blockchain-101/feed/',
                 'https://cryptocurrencynews.com/info/ethereum-101/feed/',
                 'https://cryptocurrencynews.com/info/bitcoin-101/feed/',
                 'https://cryptocurrencynews.com/info/feed/',
                 'https://news.bitcoin.com/feed/',
                 'https://www.cryptoglobe.com/rss/feed.xml',
                 'https://crypto.news/feed/',
                 'https://dailyhodl.com/feed/',
                 'https://coingape.com/feed/',
                 'https://ambcrypto.com/feed/',
                 'https://beincrypto.com/feed/', 
                ]

today_only = True

def header():
    print('---')
    print('title: "Web3 Feed"')
    print('date: ' + today_dateonly(output_format="%Y-%m-%d") + 'T00:00:00+08:00')
    print('tags: [crypto, blockchain]')
    print('draft: false')
    print('---')

header()
current_source=""
next_source=""
for each_feedsource in crypto_feedlist:
    d = feedparser.parse(each_feedsource)
    for n in range(0, len(d.entries)):

        ## ----------------------------
        ## Only show today's news (UTC)
        ## ----------------------------
        if today_only == True and is_published_today(d.entries[n].published):
            
            if current_source == "":
                current_source=get_source(each_feedsource)
                print('# ' + current_source)
            else:
                next_source=get_source(each_feedsource)
                if current_source != next_source:
                    print('# ' + next_source)
                    current_source=next_source

            print('* [' + d.entries[n].title + '](' + d.entries[n].link + ') - ' +  d.entries[n].description)

        elif today_only == False:
            if current_source == "":
                current_source=get_source(each_feedsource)
                print('# ' + current_source)
            else:
                next_source=get_source(each_feedsource)
                if current_source != next_source:
                    print('# ' + next_source)
                    current_source=next_source

            print('* [' + d.entries[n].title + '](' + d.entries[n].link + ') - ' +  d.entries[n].description)
