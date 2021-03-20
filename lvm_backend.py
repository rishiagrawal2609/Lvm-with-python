import subprocess

def checkAvailableDisks():
    print(subprocess.run("lsblk"))

def VolList():
    VolumeList = []
    Vol=int(input("Number of volume you want to add to Volume Group: "))
    for i in range(Vol):
        dName=input("Please add the address of drive you wanna make Logical volume: ")
        VolumeList.append(dName)
    print(f"Selected drives are {VolumeList}")
    return VolumeList

def createPhysicalVolume(VolumeList):
    for i in VolumeList:
        subprocess.run(f"pvcreate {i}")
        print(f"{i} Drive is converted to Physical Volume")
    print("All the drives are converted to Physical Volume")

def extendVolumeGroup(Volume):
        subprocess.run(f"vgextend {Volume}")
        print(f"{Volume} is added to Volume Group")

def createVolumeGroup(VolumeList):
    global volGrpName= input("Enter the name you want to give to your Volume Group: ")
    subprocess.run(f"vgcreate {volGrpName} {VolumeList[0]}")
    for i in range(1,len(VolumeList)):
        extendVolumeGroup(VolumeList[i])
    print("Volume Group created with the name {}!".format(volGrpName))

def createLogicalVolume(volGrpName):
    global logVolName= input("Enter the name you want to give to your Volume Group: ")
    logVolsize= input("Enter the size of Logical Volume you want to create(in G): ")
    subprocess.run(f"lvcreate --size {logVolsize}G  --name {logVolName}")
    print(f"Logical Volume of size {logVolsize}GB is created with the name {logVolName}")

def extendLogicalVolume(logVolName,volGrpName):
    addvol=input(f"How much you want to add extra in {logVolName}(in GB): ")
    subprocess.run(f"lvextend --size +{addvol}G /dev/{volGrpName}/{logVolName}")
    print(f"Logical Volume size increased by {addvol}")

def decreaseLogicalVolume(volGrpName,logVolName):
    print("WARNING THIS CAN DESTROY YOUR DATA AND NOT SUPPORTED IN GFS2 AND XFS FORMATS\n"*3)
    decvol = input(f"Enter the size by which you want to decrease in {logVolName}(in GB): ")
    subprocess.run(f"lvreduce --resizefs -L -{decvol} /dev/{volGrpName}/{logVolName}")
    print(f"Logical Volume size reduced by {decvol}")

def firstFormat(logVolName,volGrpName):
    print("Performing EXT4 formating for first time")
    subprocess.run(f"mkfs.ext4 /dev/{volGrpName}/{logVolName}")
    print("Format complete, disk is ready for mounting!")

def extendedFormat(logVolName,volGrpName):
    subprocess.run(f"resize2fs /dev/{volGrpName}/{logVolName}")
    print("Formated extended Volume!")

def mount(logVolName,volGrpName):
    des= input("Do you have existing dir on which you have to mount?:(Y/N) ")
    if(des == 'Y'):
        dirName = input("Add dir path you want to mount: ")
    else:
        dirname = input("Give name to dir where you want to mount: ")
        subprocess.run(f"mkdir /{dirName}")
    subprocess.run(f"mount /dev/{volGrpName}/{logVolName}")

def detailsPhysicalVolume(volname):
    print(subprocess.run(f"pvdisplay {volname}"))

def detailsPhysicalVolume(volGrpName):
    print(subprocess.run(f"vgdisplay {volGrpName}"))

def detailsPhysicalVolume(logVolName,volGrpName):
    print(subprocess.run(f"lvdisplay {volGrpName}/{logVolName}"))