flag = True
import os
while flag == True:
	print('\t\t\t\tWELCOME TO LVM MANAGER')
	print('\t\t\t\t----------------------')
	print()

	input('Press enter to continue......')

	print(""""
      		Select what you want to do:
      		1. Create a physical volume (PV).
      		2. Display the details of the PV.
      		3. Create a volume group(VG).
      		4. Display the details of VG.
      		5. Create and format a Logical Volume (LV).
      		6. Show details of the LV.
      		7. Increase the size of LV.
      		8. List hard disks and partitions.
      		9. Quit.
      		""")

	x = input('What do you want to do (Enter the number) : ')
	x = int(x)

	if x==1:
		y = input('Enter the partition name: ')
		os.system('pvcreate {}'.format(y))
	elif x==2:
		y = input('Enter name of the pv: ')
		os.system('pvdisplay {}'.format(y))
	elif x==3:
		y = input('Enter name of volume group(vg) : ')
		z = input("Enter name of the pv's which wil contribute the storage to vg (in continous way) : ")
		os.system('vgcreate {} {}'.format(y,z))
	elif x==4:
		y = input('Enter the name of vg : ')
		os.system('vgdisplay {}'.format(y))
	elif x ==5:
		y = input('Enter name of vg: ')
		z = input('Enter name of lv: ')
		a = input('Enter size of lv: ')
		os.system('lvcreate --size {}  --name {}  {}'.format(a,z,y))
		os.system('mkfs.ext4 /dev/{}/{}'.format(y,z))
	elif x==6:
		y = input('Enter name of vg: ')
		z = input('Enter name of lv: ')
		os.system('lvdisplay {}/{}'.format(y,z))
	elif x == 7:
		y = input('Enter name of lv (as vg_name/lv_name): ')
		z = input('Enter the size and units to be extended (as size {G,M,T}): ')
		os.system('lvextend --size +{}  {}'.format(z,y))
		os.system('resize2fs /dev/{}'.format(y))
	elif x == 8:
		os.system('fdisk -l')
	elif x == 9:
		flag = False
		break
	else:
		print('no matches found')
input()
os.system('clear')
