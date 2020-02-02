echo HI
for i in {2010..2017}
do
		sudo mkdir $i
	cd $i
	for z in {1..12}
	do
		sudo mkdir $z
	cd $z
	for j in {1..3}
	do
		sudo touch file$j
	done
	cd ../
done
cd ../
done
