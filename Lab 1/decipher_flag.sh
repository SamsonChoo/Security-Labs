for i in {1..256}
do
    python3 shiftcipher.py -i flag -o flag$i.png -k $i -m d -t b
done