#!/usr/bin/env python3
"""
Güner AV - Backlink & Dijital Ayak İzi İstihbarat Aracı
Hedef rakip domainlerin internette nereden link ve referans aldığını (dizinler, forumlar, haberler, sosyal medya) bulur.
"""

import sys
import os
import json
import urllib.parse
from ddgs import DDGS

def find_backlinks_and_mentions(target_domain, max_results=15):
    print(f"\n🔍 Hedef taranıyor: {target_domain}...")
    ddgs = DDGS()
    
    # 1. Kendi sitesi hariç domain adı geçen sayfalar ("domain.com" -site:domain.com)
    query_backlink = f'"{target_domain}" -site:{target_domain}'
    print(f"  > Backlink sorgusu: {query_backlink}")
    
    results = []
    try:
        raw = list(ddgs.text(query_backlink, max_results=max_results))
        for r in raw:
            url = r.get('href', '')
            title = r.get('title', '')
            snippet = r.get('body', '')
            netloc = urllib.parse.urlparse(url).netloc.replace('www.', '')
            
            # Kendi domainini ve arama motorlarını filtrele
            if target_domain not in netloc:
                results.append({
                    'referring_domain': netloc,
                    'title': title,
                    'url': url,
                    'snippet': snippet
                })
    except Exception as e:
        print(f"  [Hata]: {e}")
        
    return results

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else 'ozsanavbayi.com'
    print("=" * 65)
    print(f"🌐 GÜNER AV - BACKLINK RECON (Ayak İzi Dedektifi)")
    print(f"🎯 Hedef Domain: {target}")
    print("=" * 65)
    
    links = find_backlinks_and_mentions(target, max_results=20)
    print(f"\n📊 Bulunan Referans & Backlink Kaynakları ({len(links)} adet):")
    print("-" * 65)
    
    for idx, l in enumerate(links, 1):
        print(f"[{idx:02d}] 🔗 Kaynak Domain: {l['referring_domain']}")
        print(f"     Başlık: {l['title']}")
        print(f"     URL: {l['url']}")
        print(f"     Özet: {l['snippet'][:120]}...")
        print()

if __name__ == '__main__':
    main()
