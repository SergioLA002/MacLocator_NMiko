# Localizador de Direcciones MAC en Redes Cisco


Este programa permite localizar la dirección MAC proporcionada en una red de switches Cisco utilizando comandos a través de la librería Netmiko. Realiza un rastreo iterativo entre switches conectados mediante CDP (Cisco Discovery Protocol) hasta encontrar la MAC o no encontrar más vecinos.

## CARACTERISTICAS
-Realiza consultas en la tabla de direcciones MAC de un switch para encontrar el puerto asociado.

-Obtiene información detallada sobre la interfaz donde se encuentra la dirección MAC.

-Identifica dispositivos vecinos utilizando CDP para continuar la búsqueda en switches conectados.

## Requisitos Previos
Python 3.8 o superior

-Librería Netmiko
`pip install netmiko`

-Acceso a la red donde estén los switches Cisco.

-Credenciales de los dispositivos Cisco:

EJEMPLO:

Usuario: cisco

Contraseña: cisco

## Configuración Inicial

La configuración inicial inicia desde  `SWITCH_ACTUAL`. Configurando la dirección de el switch, ademas de las credenciales de autenticación.
    
	SWITCH_ACTUAL = {
		"device_type": "cisco_ios",
   	 "host": "192.168.1.1",
   	 "username": "cisco",
    	"password": "cisco"
    
Incia el programa e introduce la mac solicitada en la terminal (FFFF.FFFFF.FFFF):

Ejemplo de uso con la siguiente mac 0001.42AB.CDEF: 

    introduce la mac buscada en este formato "FFFF.FFFF.FFFF": 0001.42AB.CDEF

## Funciones Principales:
```
show_mac_address_table: Busca la MAC en la tabla de direcciones del switch actual.

show_interface: Obtiene información detallada de la interfaz donde se encuentra la MAC.

cdp_neighbor_details: Identifica vecinos conectados en la interfaz correspondiente.

nueva_conexion: Establece una nueva conexión al dispositivo vecino.
```
### Lógica Principal
Realiza la búsqueda iterativa a través de dispositivos vecinos hasta encontrar la dirección MAC o terminar el rastreo.

### Autores
Nombre del desarrollador: Sergio Aldana
