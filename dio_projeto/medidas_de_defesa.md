# Medidas de defesa contra ransomware e keyloggers

## Antivírus e EDR

Antivírus tradicionais identificam ameaças conhecidas por assinaturas. Soluções modernas de EDR (*Endpoint Detection and Response*) observam comportamentos suspeitos, como:

- Criptografia em massa de arquivos.
- Criação repentina de arquivos `.enc`.
- Processos tentando acessar muitos arquivos.
- Captura persistente de teclas.
- Conexões de saída incomuns.

## Firewall

O firewall ajuda a controlar conexões de rede. Ele pode bloquear comunicações suspeitas de saída, impedir que um malware envie dados para servidores externos e limitar acessos não autorizados.

## Sandboxing

Sandboxing é a execução de um programa em um ambiente isolado. Isso permite observar seu comportamento sem colocar o sistema principal em risco.

Exemplos:

- Máquina virtual.
- Contêiner isolado.
- Ambiente de análise de malware.
- Conta de usuário sem privilégios administrativos.

## Backups

Backups são a defesa mais importante contra ransomware. Eles devem ser:

- Frequentes.
- Testados.
- Mantidos offline ou imutáveis.
- Protegidos por senha e criptografia.
- Armazenados fora do alcance de um processo comprometido.

Mesmo se arquivos forem criptografados, um backup íntegro permite restaurar os dados sem pagar resgate.

## Atualizações

Manter sistema operacional, navegadores, antivírus e aplicativos atualizados reduz vulnerabilidades exploráveis por malwares.

## Autenticação multifator

Mesmo que um keylogger capture uma senha, a autenticação multifator (MFA) dificulta o acesso indevido à conta, porque exige um segundo fator de verificação.

## Conscientização do usuário

Muitos ataques começam por engenharia social:

- E-mails falsos.
- Links suspeitos.
- Anexos inesperados.
- Instaladores falsos.
- Mensagens pedindo senha ou código de verificação.

Nunca abra anexos desconhecidos nem instale programas de fontes não confiáveis.

## Princípio do menor privilégio

Cada usuário e programa deve ter apenas as permissões necessárias. Assim, se um malware for executado, ele terá menos capacidade de danificar o sistema ou acessar dados sensíveis.

## Monitoramento

É importante observar:

- Processos desconhecidos.
- Arquivos criados em massa.
- Extensões alteradas.
- Tráfego de rede anormal.
- Tentativas de acesso a arquivos sensíveis.
- Programas iniciados automaticamente com o sistema.
