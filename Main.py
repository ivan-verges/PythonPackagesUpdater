from subprocess import call, check_output

#Updates Current PIP Module to Latest Version
print ("Updating Pip")
call("python -m pip install --upgrade pip", shell=True)

#Gets All Outdated Modules from PIP
print ("Getting Outdated Packages")
packages = check_output(["pip", "list", "-o"])

#Converts the Response from Bytes to String
packages = packages.decode("utf-8")

#Converts the String to a String Array Separated By the "Return" and "New Line" Characters
packages = packages.split("\r\n")

#Removes the First 2 Lines from the Array (Header and Separation Lines) and the Last One (Empty)
packages = packages[2 : -1]

#Updates Every Outdated Package
for package in packages:

    #Gets the Package Name from the Array
    tmp = package.split(" ")[0]

    #Prints the Current Package Name and Updates it
    print ("Updating Package: " + tmp)
    call("pip install --upgrade " + tmp, shell=True)
