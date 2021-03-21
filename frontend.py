import lvm_backend as lvm
a = True
while a == True: 
    lvm.clearScreen()
    lvm.introHeader()
    print("What You would like to do?")
    print("""
        1. Create New Logical Volume\n
        2. Extend the size of the Logical Volume\n
        3. Convert drives to Physical Volume\n
        4. Add Physical volumes to the Volume Group\n
        5. Check details about the Logical Volumes and related\n
        6. exit
    """)

    uc = int(input("Enter the option: "))
    lvm.clearScreen()
    if (uc == 1):
        lvm.introHeader()
        lvm.checkAvailableDisks()
        vol = lvm.VolList()
        lvm.createPhysicalVolume(vol)
        vg = lvm.createVolumeGroup(vol)
        lv = lvm.createLogicalVolume(vg)
        lvm.firstFormat(lv,vg)
        lvm.mount(lv,vg)
        continue

    elif (uc ==2):
        lvm.introHeader()
        volGrpName = input("Enter the name of your Volume Group: ")
        logVolName = input("Enter the name of your Logical volume: ")
        lvm.extendLogicalVolume(volGrpName,logVolName)
        lvm.extendedFormat(logVolName,volGrpName)
        continue

    elif (uc == 3):
        lvm.introHeader()
        vol = lvm.VolList()
        lvm.createPhysicalVolume(vol)
        continue

    elif (uc == 4):
        lvm.introHeader()
        no = int(input("How many Physical Volume to add: "))
        for i in range(no):
            vol = input("Enter volume you want to add: ")
            lvm.extendVolumeGroup(vol)
        continue

    elif (uc == 5):
        lvm.introHeader()
        b=True
        while b == True:
            print("Select one you want the details:\n 1.Physical Volume\n 2.Volume Group \n 3. Logical Volume\n 4.exit")
            choose = int(input("Your selection: "))
            if (choose == 1):
                lvm.detailsPhysicalVolume()
                continue
            elif (choose == 2):
                lvm.detailsVolumeGroup()
                continue
            elif (choose == 3):
                lvm.detailsLogicalVolume()
                continue
            elif (choose == 4):
                b= False
                continue
            else:
                print("No option Like that available, please select \
                    between 1 to 4")
                continue
        continue
    elif (uc == 6):
        a = False
        continue
    else:
        print("No option Like that available, please select \
                    between 1 to 6")
        continue

print(""" 
████████ ██   ██  █████  ███    ██ ██   ██ ███████     ███████  ██████  ██████      ██    ██ ███████ ██ ███    ██  ██████      ████████ ██   ██ ██ ███████     ████████  ██████   ██████  ██      
   ██    ██   ██ ██   ██ ████   ██ ██  ██  ██          ██      ██    ██ ██   ██     ██    ██ ██      ██ ████   ██ ██              ██    ██   ██ ██ ██             ██    ██    ██ ██    ██ ██      
   ██    ███████ ███████ ██ ██  ██ █████   ███████     █████   ██    ██ ██████      ██    ██ ███████ ██ ██ ██  ██ ██   ███        ██    ███████ ██ ███████        ██    ██    ██ ██    ██ ██      
   ██    ██   ██ ██   ██ ██  ██ ██ ██  ██       ██     ██      ██    ██ ██   ██     ██    ██      ██ ██ ██  ██ ██ ██    ██        ██    ██   ██ ██      ██        ██    ██    ██ ██    ██ ██      
   ██    ██   ██ ██   ██ ██   ████ ██   ██ ███████     ██       ██████  ██   ██      ██████  ███████ ██ ██   ████  ██████         ██    ██   ██ ██ ███████        ██     ██████   ██████  ███████ 
                                                                                                                                                                                                  
""")