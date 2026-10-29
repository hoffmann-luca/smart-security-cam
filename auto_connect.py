import os

TestName = "TestName"
TestKey = "TestKey"

def writeWlan(WName, WKey):
    wpa_sup = "network={\n"
    wpa_sup += "    ssid="+WName+"\n"
    wpa_sup += "    psk="+WKey+"\n"
    wpa_sup += "}"
    #print(wpa_sup + " < /etc/wpa_supplicant/wpa_supplicant.conf")
    #os.system(wpa_sup + " < /etc/wpa_supplicant/wpa_supplicant.conf")
    writeIn = open("wpa_supp")
    
writeWlan(TestName, TestKey)
