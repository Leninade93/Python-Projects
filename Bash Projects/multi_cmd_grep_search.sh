!#/bin/bash
let start_time=$(date +%s)
echo -n "Total Matches: " && (whois 8.8.8.8 | grep -c "Comment:") && (whois 8.8.8.8 | grep --colour "Comment:") 
sleep 2.5s
let end_time=$(date +%s)
let runtime=end_time-start_time
echo -n "Script Complete in: $runtime second(s). Currently only returns integer values."
