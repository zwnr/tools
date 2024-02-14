# "Make a selection" loop
while True:
 try:
   selection = int(input("1 - NID\n"
                         "2 - MCPE\n"
                         "3 - Study Guides\n"
                         "\n"
                         "Enter a selection: "))
   if selection in range(1, 3):
      break
   else:
      print("1 - NID\n"
            "2 - MCPE\n"
            "3 - Study Guides\n"
            "\n"
            "ERROR: INVALID NUMBER! Try again: ")
 except ValueError:
      print("ERROR: INVALID SELECTION! Press enter.")
    
# Choose NID model
if selection == 1:
 while True:
   try:
     nid_vendor = int(input("1 - Accedian\n"
                            "2 - Adva\n"
                            "3 - Ciena\n"
                            "4 - Cisco\n"
                            "5 - RAD\n"
                            "\n"
                            "Enter a selection: "))
     if nid_vendor in range(1, 6):
        break
     else:
         print("1 - Accedian\n"
               "2 - Adva\n"
               "3 - Ciena\n"
               "4 - Cisco\n"
	             "5 - RAD\n"
               "\n"
               "ERROR: INVALID NUMBER! Try again: ")
   except ValueError:
    print("ERROR: INVALID SELECTION! Press enter.")  

 # Choose NID Stage     
 if nid_vendor == 1:
   print(~/accedian_stage1.txt)
 elif nid_vendor == 2:
   print(~/adva_ge114pro_stage1.txt)
 elif nid_vendor == 3:
   print(~/ciena5142_stage1.txt)
 elif nid_vendor == 4:
   print(~/cisco_nid_stage1.txt)
 elif nid_vendor == 5:
   print(~/rad_203_stage1.txt)
             
# Choose MCPE model
elif selection == 2:
 while True:
  try:
    mcpe_vendor = int(input("1 - Adtran\n"
                  	        "2 - Cisco\n"
                            "\n"
                            "Enter a selection: "))
    if mcpe_vendor in range(1, 3):
	    break
    else:
            print("1 - Adtran\n"
                  "2 - Cisco\n"
                  "\n"
                  "ERROR: INVALID NUMBER! Try again: ")
  except ValueError:
            print("ERROR: INVALID SELECTION! Please enter a number.")  

 if mcpe_vendor == 1:
   print(~/adtran_stage1.cfg)
 elif mcpe_vendor == 2:
   print(~/cisco_stage1.cfg)
       
# Choose STUDY GUIDE
 #elif selection == 3:
   #while True:
