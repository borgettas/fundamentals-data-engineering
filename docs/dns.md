Para desabilitar o gerenciamento automático de DNS no Fedora e permitir que o FortiClient use suas próprias configurações de DNS, você pode seguir os passos abaixo. Isso geralmente envolve a configuração do NetworkManager para não interferir nas configurações de DNS.

### Passos para Desabilitar o DNS no Fedora

1. **Edite o arquivo de configuração do NetworkManager**:
   Abra um terminal e edite o arquivo de configuração do NetworkManager:
   ```bash
   sudo nano /etc/NetworkManager/NetworkManager.conf
   ```

2. **Adicione ou modifique a seção `[main]`**:
   Adicione a linha `dns=none` na seção `[main]` do arquivo. Se a seção não existir, você pode criá-la. O arquivo deve ficar assim:
   ```
   [main]
   dns=none
   ```

3. **Salve e saia do editor**:
   No `nano`, você pode fazer isso pressionando `CTRL + O` para salvar e `CTRL + X` para sair.

4. **Reinicie o NetworkManager**:
   Para aplicar as alterações, reinicie o serviço do NetworkManager:
   ```bash
   sudo systemctl restart NetworkManager
   ```

5. **Verifique o arquivo `/etc/resolv.conf`**:
   Após reiniciar o NetworkManager, você pode editar o arquivo `/etc/resolv.conf` para adicionar os servidores DNS que você deseja usar. Por exemplo:
   ```bash
   sudo nano /etc/resolv.conf
   ```
   Adicione as linhas:
   ```
   nameserver 8.8.8.8
   nameserver 8.8.4.4
   ```
   Salve e saia do editor.

6. **Conecte-se ao FortiClient**:
   Agora, você pode abrir o FortiClient e conectar-se à VPN. O FortiClient deve usar as configurações de DNS que você definiu manualmente.

### Observações

- **Persistência**: Com `dns=none`, o NetworkManager não irá mais gerenciar o DNS, então você precisará garantir que o arquivo `/etc/resolv.conf` esteja configurado corretamente sempre que necessário.
- **Outros gerenciadores de rede**: Se você estiver usando outro gerenciador de rede (como `systemd-resolved`), você pode precisar desativá-lo ou configurá-lo de maneira semelhante.
- **Testes**: Após fazer essas alterações, teste a conexão VPN e verifique se a resolução de DNS está funcionando conforme esperado.

Se você tiver mais perguntas ou precisar de mais assistência, sinta-se à vontade para perguntar!