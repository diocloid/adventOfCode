#!/bin/sh

# USAGE
# ./setup.sh  4

DAY=$1

touch 2023/data/day$DAY.test.txt
echo "https://adventofcode.com/2023/day/${DAY}/input"
curl "https://adventofcode.com/2023/day/${DAY}/input" --compressed -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/201001 01 Firefox/120.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://adventofcode.com/2023/day/2' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: session=53616c7465645f5f9b5ed08c48b7d8e17f5e35e3e315add7ab8e8cffd6ef74fa8f2076d72a5ff02eea29f43690b7d038bd03c33d8837c224b60c590baf07c871' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'TE: trailers' -o 2023/data/day$DAY.prod.txt