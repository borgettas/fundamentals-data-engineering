# Ajustando Limites de Rede Cabeada (Fedora 40)

#### Verifique as Configurações de Rede
``` bash
nmcli device status
```

Caso a mesama esteja desconectada, conecte usando:
``` bash
nmcli device connect <DEVICE>
``` 

#### Verifique a Configuração do MTU:
O tamanho da unidade máxima de transmissão (MTU) pode afetar a velocidade da conexão. Tente ajustar o MTU para um valor diferente (por exemplo, 1400 ou 1492):

``` bash
sudo ip link set dev <DEVICE> mtu 1400
```