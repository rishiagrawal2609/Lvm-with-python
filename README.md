# Automating the LVM in Linux using Python Script
### A script that takes you from all the logical volume management hassle free and easily.

Note: This script is only for RHEL 8 OS and fully tested over it.

# Setup Instructions:
#### Base Requirement:
- The script only works on the RHEL 8 as a OS.
- To use the script you need to login as a root user.
- Run `fdisk -l` before using the script to check drives are connected or not.
- Your base OS(RHEL 8) sholuld have git installed.

If all the requirement is clear, then you are good to go.

#### Downloading and running the script
To download the script use the following command
```dotnetcli
 # git clone https://github.com/rishiagrawal2609/Lvm-with-python.git
```
After downloading, migrate to the folder first
```dotnetcli
# cd ./Lvm-with-python
```
After this, run the command:
```dotnetcli
# python3 lvmConfig.py
```
And its done, run the script according to the need.

# About the Script
#### The script can be used for the following usecases:
- To create new Logical Volume from scratch.
- To extend the size of the existing Logical Volume.
- To convert new drive to physical volume.
- To add physical volume to existing volume group.
- To display the details of LVM related resources.

If you have any usecase above, the script is for you.

# Contact
Any quries, Please raise in the issues tab or If you have any idea to add you can send PR or <b>[mail me](mailto:rishiagrawal2609@gmail.com)</b>