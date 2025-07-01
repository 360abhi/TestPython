# > overwrite >> append
echo "Hello file" > hello.txt

# pipes send output of one command to input of other command
cat myfile.txt | grep "error" || echo "No errors Found"

# passes text conten to grep which prints line with error if no lin then only || triggers
