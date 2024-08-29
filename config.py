CLIENT_IP="192.168.128.57" # Ip do agent do cliente
APLICATION_IP="192.168.100.107" # Ip da aplicação
APLICATION_PORT="5000" # Porta utilizada pela aplicação
APLICATION_PROTOCOL="http" # Protocolo de comunicação, http se  SSL_CERTIFICATE = False, se não https
DEBUG_MODE=True # Ativado = True, Desativado = False
SSL_CERTIFICATE=False #Ativado = True, Desativado = False

# Se SSL_CERTIFICATE = True:
CRT_PATH="" # Caminho do arquivo .crt
KEY_PATH="" # Caminho do arquivo .key