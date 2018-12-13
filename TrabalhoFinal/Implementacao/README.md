# Execução

Para o sistema funcionar da forma como esperada, os scripts devem ser executados na seguinte ordem:

1- O middleware (nameMiddleware)

2- Os servidores de nomes (nameServer), quantos forem desejados, lembrando que cada execução deve ser feita com uma porta diferente.

3- Os serviços que existirão no sistema, no caso server1 e server2. Mas qualquer serviço que possuir as funções connectMiddleware, o protocolo de comunicação com o cliente e conhecerem o endereço do middleware podem ser executados. 



