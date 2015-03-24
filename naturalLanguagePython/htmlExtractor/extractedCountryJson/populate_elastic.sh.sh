#!/bin/sh

for i in *.json;
	do curl -XPUT "http://localhost:9200/country/data/`echo $i | sed 's/\.json//'`" -d "`cat $i`";
done