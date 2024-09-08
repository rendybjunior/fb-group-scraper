cat data/header.csv | head -n1 > data/merged.csv 
for f in data/messages_*.csv; do cat "`pwd`/$f" | tail -n +2 >> data/merged.csv; done