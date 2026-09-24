#!/bin/bash
# Güner AV Rakip ve SERP Analizini Tek Tıkla Çalıştırır

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "=========================================================="
echo "🎯 Güner AV - SERP & Rakip İstihbarat Botu"
echo "=========================================================="

if [ ! -d "venv" ]; then
    echo "📦 Sanal ortam kuruluyor..."
    python3 -m venv venv
    ./venv/bin/pip install --quiet beautifulsoup4 requests ddgs
fi

./venv/bin/python scanner.py
echo ""
echo "✅ Tarama bitti! Raporu incelemek için:"
echo "   open RAKIP_ANALIZ_VE_STRATEJI_RAPORU.md"
