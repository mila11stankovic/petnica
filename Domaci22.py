rečnik = {"brzo":{"sinonimi":["hitro", "žurno"], "antonimi":["sporo", "polako"]},"toplo":{"sinonimi":["vrelo", "zagrejano"], "antonimi":[ "hladno", "ledeno"]}, "beba":{"sinonimi":["novorođenče", "čedo"], "antonimi":["baka", "deka"]}}
print(rečnik["brzo"]["sinonimi"]) 
print(rečnik["toplo"]["antonimi"]) 
print(rečnik["beba"]["sinonimi"][0]) 
print(rečnik["brzo"]["antonimi"][1]) 

for reč in rečnik.keys():
    
    print("Reč: ", reč) 
    sin = "Sinonimi: "
    ant = "Antonimi: "

    for sinonim in rečnik[reč]["sinonimi"]:
        sin += sinonim + ", "
    print(sin[:-2])

    for antonim in rečnik[reč]["antonimi"]:
        ant += antonim + ", "    
    print(ant[:-2] + "\n") 

   


   