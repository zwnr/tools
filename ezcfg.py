#if selection in (1, 2, 3):
#  config_file_map = {
#    1: "accedian_stage1.txt",
#    2: "adva_ge114pro_stage1.txt",
#    3: "ciena5142_stage1.txt",
#    4: "cisco_nid_stage1.txt",
#    5: "rad_203_stage1.txt",
#  }
#  config_file = config_file_map[nid_vendor]
#
#  with open(config_file, "r") as file:
#    content = file.read()
#    print(content)
#else:
#  print(f"Invalid nid_vendor value: {nid_vendor}")
#
#except FileNotFoundError as e:
#  print(f"Error: File not found: {e.filename}")
#except Exception as e:
#  print(f"An unexpected error occurred: {e}")
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
    generate_cfg = "accedian_stage1.txt"
    with open(generate_cfg, "r") as file:
        print(file.read())
elif nid_vendor == 2:
    generate_cfg = "adva_ge114pro_stage1.txt"
    with open(generate_cfg, "r") as file:
        print(file.read())
elif nid_vendor == 3:
    generate_cfg = "ciena5142_stage1.txt"
    with open(generate_cfg, "r") as file:
        print(file.read())
elif nid_vendor == 4:
    generate_cfg = "cisco_nid_stage1.txt"
    with open(generate_cfg, "r") as file:
        print(file.read())
elif nid_vendor == 5:
    generate_cfg = "rad_203_stage1.txt"
    with open(generate_cfg, "r") as file:
        print(file.read())
        
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
        generate_cfg = "adtran_stage1.cfg"
        with open(generate_cfg, "r") as file:
            print(file.read())
elif mcpe_vendor == 2:
   generate_cfg = "cisco_stage1.cfg"
   with open(generate_cfg, "r") as file:
       print(file.read())
   
# Choose STUDY GUIDE
#elif selection == 3:
    #while True: