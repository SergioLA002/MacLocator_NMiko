from netmiko import ConnectHandler

ip_inicial = input("Ingresa la ip del switch principal (255.255.255.255): ")

SWITCH_ACTUAL = {"device_type": "cisco_ios","host": ip_inicial,"username": "cisco","password": "cisco"}
               #b05c.da22.8039

def show_mac_address_table(conexion, mac):
    connection = ConnectHandler(**conexion)
    salida = connection.send_command("show mac address-table")
    hostname = connection.send_command("show running-config | include hostname")

    buscar = salida.find(mac) 

    if buscar != -1:
        puerto = salida.split(mac)[1].split()[1]
        if (puerto == "Fa1/0/47" or puerto == "Fa1/0/48") or (puerto == "FastEthernet1/0/47" or puerto == "FastEthernet1/0/48"):
            print("\nLa MAC", mac, "no se encuentra en dispositivo", hostname[9::], " Buscando...")
        else: 
            print("\nLa MAC:",mac, "se encuentra en el puerto"  , puerto, "del dispositivo", hostname[9::])
        return puerto
    else:
        print (f"\n Imposible Encontrar la mac. Pruebe Otra vez")
        return buscar

def show_interface(conexion, port):
    connection = ConnectHandler(**conexion)
    comando = "show interface " + port
    salida = connection.send_command(comando)

    interface = salida.split()[0]
    return interface

def cdp_neighbor_details(conexion, interface):
    connection = ConnectHandler(**conexion)
    salida = connection.send_command("show cdp neighbors detail")

    texto = "Interface: " + interface
    dispositivos = salida.split("-------------------------")
    
    for i in dispositivos:
        if texto in i:
              filtro = i.split("Platform")[0]
              segundofiltro = filtro.split("IP address: ")[1]
              #print("Vecino encontrado en ", texto, ", buscando en otro dispositivo...")
              return segundofiltro.strip()
    return -1

def nueva_conexion(IP):
    print("\nConectando a ", IP) 
    SWITCH_VECINO = {"device_type": "cisco_ios","host": IP,"username": "cisco","password": "cisco",}
    return SWITCH_VECINO

mac_buscada = input('introduce la mac buscada en este formato "FFFF.FFFFF.FFFF": ')

while True: 
    puerto = show_mac_address_table(SWITCH_ACTUAL, mac_buscada)
    if puerto == -1:
        break
    interfaz = show_interface(SWITCH_ACTUAL, puerto)
    ip = cdp_neighbor_details(SWITCH_ACTUAL, interfaz)
    if ip == -1:
        break
    SWITCH_ACTUAL = nueva_conexion(ip)

    #f430.b9a0.c3e8
    #00e0.4c68.000d