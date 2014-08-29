# read command line arguments from command line
ARG1=$1
ARG2=$2

echo $ARG1
echo $ARG2

# read user input from command line
echo -n "Enter your name and press [ENTER]: "
read name
echo $name