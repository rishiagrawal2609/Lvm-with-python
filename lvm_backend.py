import subprocess
import os 
def checkAvailableDisks():
    print(subprocess.run("lsblk"))

def VolList():
    global VolumeList
    VolumeList = []
    Vol=int(input("Number of volume you want to add to Volume Group: "))
    for i in range(Vol):
        dName=input("Please add the address of drive you wanna make Logical volume: ")
        VolumeList.append(dName)
    print(f"Selected drives are {VolumeList}")
    return VolumeList

def createPhysicalVolume(VolumeList):
    for i in VolumeList:
        os.system(f"pvcreate {i}")
        print(f"{i} Drive is converted to Physical Volume")
    print("All the drives are converted to Physical Volume")

def extendVolumeGroup(Volume, vgname):
        os.system(f"vgextend {vgname} {Volume}")
        print(f"{Volume} is added to Volume Group")

def createVolumeGroup(VolumeList):
    volGrpName = input("Enter the name you want to give to your Volume Group: ")
    os.system(f"vgcreate {volGrpName} {VolumeList[0]}")
    for i in range(1,len(VolumeList)):
        extendVolumeGroup(VolumeList[i],volGrpName)
    print("Volume Group created with the name {}!".format(volGrpName))
    return volGrpName

def createLogicalVolume(volGrpName):
    logVolName = input("Enter the name you want to give to your Logical Volume: ")
    logVolsize= input("Enter the size of Logical Volume you want to create(in G): ")
    os.system(f"lvcreate --size {logVolsize}G  --name {logVolName} {volGrpName}")
    print(f"Logical Volume of size {logVolsize}GB is created with the name {logVolName}")
    return logVolName

def extendLogicalVolume(volGrpName,logVolName):
    addvol=input(f"How much you want to add extra in {logVolName}(in GB): ")
    os.system(f"lvextend --size +{addvol}G /dev/{volGrpName}/{logVolName}")
    print(f"Logical Volume size increased by {addvol}")
    os.system("df -h")

def decreaseLogicalVolume(volGrpName,logVolName):
    print("WARNING THIS CAN DESTROY YOUR DATA AND NOT SUPPORTED IN GFS2 AND XFS FORMATS\n"*3)
    decvol = input(f"Enter the size by which you want to decrease in {logVolName}(in GB): ")
    os.system(f"lvreduce --resizefs -L -{decvol} /dev/{volGrpName}/{logVolName}")
    print(f"Logical Volume size reduced by {decvol}")

def firstFormat(logVolName,volGrpName):
    print("Performing EXT4 formating for first time")
    os.system(f"mkfs.ext4 /dev/{volGrpName}/{logVolName}")
    print("Format complete, disk is ready for mounting!")

def extendedFormat(logVolName,volGrpName):
    os.system(f"resize2fs /dev/{volGrpName}/{logVolName}")
    print("Formated the extended Volume!")

def mount(logVolName,volGrpName):
    des= input("Do you have existing dir on which you have to mount?:(Y/N) ")
    dirname = ''
    if(des == 'Y'):
        dirName = input("Add dir path you want to mount: ")
    else:
        dirName = input("Give name to dir where you want to mount: ")
        os.system(f"mkdir /{dirName}")
    os.system(f"mount /dev/{volGrpName}/{logVolName} /{dirName}")
    os.system("df -h")
    print(f"Disk has mounted over the /{dirName}")

def detailsPhysicalVolume():
    pv = input("Enter the Physical Volume which you want to see details: ")
    print(os.system(f"pvdisplay {pv}"))

def detailsVolumeGroup():
    vg = input("Enter the Volume Group which you want to see details: ")
    print(os.system(f"vgdisplay {vg}"))

def detailsLogicalVolume():
    vg = input("Enter the Volume Group where the Logical Volume is located: ")
    lv = input("Enter the logical Volume which you want to see details: ")
    print(os.system(f"lvdisplay {vg}/{lv}"))

def introHeader():
    print(""" 
    $$\   $$\           $$\                           $$\   $$\    $$\ $$\      $$\                     $$\   $$\     $$\             $$$$$$$\ $$\     $$\ $$$$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\ 
    $$ |  $$ |          \__|                          $$ |  $$ |   $$ |$$$\    $$$ |                    \__|  $$ |    $$ |            $$  __$$\\$$\   $$  |\__$$  __|$$ |  $$ |$$  __$$\ $$$\  $$ |
    $$ |  $$ | $$$$$$$\ $$\ $$$$$$$\   $$$$$$\        $$ |  $$ |   $$ |$$$$\  $$$$ |      $$\  $$\  $$\ $$\ $$$$$$\   $$$$$$$\        $$ |  $$ |\$$\ $$  /    $$ |   $$ |  $$ |$$ /  $$ |$$$$\ $$ |
    $$ |  $$ |$$  _____|$$ |$$  __$$\ $$  __$$\       $$ |  \$$\  $$  |$$\$$\$$ $$ |      $$ | $$ | $$ |$$ |\_$$  _|  $$  __$$\       $$$$$$$  | \$$$$  /     $$ |   $$$$$$$$ |$$ |  $$ |$$ $$\$$ |
    $$ |  $$ |\$$$$$$\  $$ |$$ |  $$ |$$ /  $$ |      $$ |   \$$\$$  / $$ \$$$  $$ |      $$ | $$ | $$ |$$ |  $$ |    $$ |  $$ |      $$  ____/   \$$  /      $$ |   $$  __$$ |$$ |  $$ |$$ \$$$$ |
    $$ |  $$ | \____$$\ $$ |$$ |  $$ |$$ |  $$ |      $$ |    \$$$  /  $$ |\$  /$$ |      $$ | $$ | $$ |$$ |  $$ |$$\ $$ |  $$ |      $$ |         $$ |       $$ |   $$ |  $$ |$$ |  $$ |$$ |\$$$ |
    \$$$$$$  |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |      $$$$$$$$\\$  /   $$ | \_/ $$ |      \$$$$$\$$$$  |$$ |  \$$$$  |$$ |  $$ |      $$ |         $$ |       $$ |   $$ |  $$ | $$$$$$  |$$ | \$$ |
    \______/ \_______/ \__|\__|  \__| \____$$ |      \________|\_/    \__|     \__|       \_____\____/ \__|   \____/ \__|  \__|      \__|         \__|       \__|   \__|  \__| \______/ \__|  \__|
                                    $$\   $$ |                                                                                                                                                   
                                    \$$$$$$  |                                                                                                                                                   
                                    \______/                                                                                                                                                    
                                                                                                                                                                                By Rishi Agrawal
    """)

def clearScreen():
    subprocess.run("clear")