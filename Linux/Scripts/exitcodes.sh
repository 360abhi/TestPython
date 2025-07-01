# All non zero codes are failure codes

echo "$?"

ls /fakepath
echo "$?"

cp myfile.txt /some/folder
if [ "$?" -ne 0 ];then
    echo "copy failed"
    exit 1
else
    echo "copy success"
fi