echo "14" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio14/direction
echo "1" > /sys/class/gpio/gpio14/value
sleep 30
echo "0" > /sys/class/gpio/gpio14/value
echo "14" > /sys/class/gpio/unexport
