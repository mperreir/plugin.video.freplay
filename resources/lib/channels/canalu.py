#-*- coding: utf-8 -*-   
import urllib2
import CommonFunctions
common = CommonFunctions
from resources.lib import utils      
import re

title=['Canal U']
img=['canalu']
readyForUse=True          

def list_shows(channel,folder):
  shows=[]
  shows.append( [channel,'1','Sciences juridiques et politiques','','shows'] )
  shows.append( [channel,'2','Sciences fondamentales','','shows'] )
  shows.append( [channel,'3','Sciences de l�ing�nieur','','shows'] )
  shows.append( [channel,'4','Sciences humaines, sociales, de l��ducation et de l�information','','shows'] )
  shows.append( [channel,'5','Environnement et d�veloppement durable','','shows'] )
  shows.append( [channel,'6','Lettres, Arts, Langues et Civilisations','','shows'] )
  shows.append( [channel,'7','Economie et Gestion','','shows'] )
  shows.append( [channel,'8','Sciences de la sant� et du sport','','shows'] )
  
  return shows
  
def list_videos(channel,id):
  videos=[]  
  
  filePath=utils.downloadCatalog('http://www.canal-u.tv/themes/format.rss/theme.%s/podcast.1?xts=248546&xtor=RSS-1' % id, 'canalu%s.xml' % id,False)    
  xml=open(filePath).read().replace('\xe9', 'e').replace('\xe0', 'a') 
  items=common.parseDOM(xml, "item")
  for i in range(0, len(items)):  
    if common.parseDOM(items[i], "enclosure", ret = "type")[0]=='video/mpeg':
      title=common.parseDOM(items[i], "title")[0].encode('utf-8')
      description=common.parseDOM(items[i], "description")[0].encode('utf-8')
      date=common.parseDOM(items[i], "pubDate")[0][0:16].encode('utf-8')
      url=common.parseDOM(items[i], "link")[0]
      
      infoLabels={ "Title": title,"Plot":description,"Aired":date, "Year":date[:4]}
      videos.append( [channel, url, title, '',infoLabels,'play'] )
      
      print title,url
  return videos

def getVideoURL(channel,url):
  html=urllib2.urlopen(url).read()
  url = re.findall('file: "(.*?).mp4",',html) [0] + '.mp4'
  return url