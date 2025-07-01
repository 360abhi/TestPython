read -p "Enter your age:" age

if [ "$age" -ge 18 ];then
    echo "You're eligible to Vote"
else
    echo "Sorry not yet eligible"
fi

read -p "What is you name" name

if [ "$name" = "Abhishek" ];then
    echo "Welcome $name"
else
    echo "Sorry you're not Abhishek you are $name"
fi

if [ -f "myfile.txt" ];then
    echo "file exists"
else
    echo "File not found"
fi

if [ -s "myfile.txt" ];then
    echo "file has something in it"
else
    echo "File is empty"
fi
