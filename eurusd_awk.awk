#!/bin/awk -f
BEGIN{
	#{print "Timestamp,Bid price,Ask price,Bid volume,Ask volume" > "eurusd_tmp.csv"};
	$1 " " $2 >= $start && $1 " " $2 <= $end;
}
