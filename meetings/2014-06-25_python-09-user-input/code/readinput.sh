# read command line arguments from command line
ARG0=$0
ARG1=$1
ARG2=$2

echo "Argument 0 is: " $ARG0
echo "Argument 1 is: " $ARG1
echo "Argument 2 is: " $ARG2

# read user input from command line
echo -n "Enter your name and press [ENTER]: "
read name
echo $name