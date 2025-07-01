greet(){
    echo "hello this is greet function"
    echo "Arguments are $1 and $2"
}
greet "Abhishek" 25


square(){
    local result=$(($1 * $1))
    echo "$result"
}

val=$(square 4)
echo "$val"


checkeven(){
    if(( $1 % 2 ==0 ));then
        return 0
    else
        return 1
    fi
}

checkeven 4
if [ $? -eq 0 ];then
    echo "Even number"
else
    echo "Odd number"
fi