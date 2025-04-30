Objetivo:** Verificar se o login com credenciais válidas redireciona para a página de produtos.


1. Acessar https://www.saucedemo.com
2. Inserir usuário "standard_user"
3. Inserir senha "secret_sauce"
4. Clicar em "Login"
5. Verificar se a URL contém "/inventory"


- Usuário: standard_user
- Senha: secret_sauce


- Página de produtos exibida (URL com `/inventory`)


- Página redirecionada corretamente
- Login confirmado pelo console





**Objetivo:** Validar que um usuário inválido gera uma mensagem de erro.


1. Acessar https://www.saucedemo.com
2. Inserir usuário "invalid_user"
3. Inserir senha "wrong_password"
4. Clicar em "Login"
5. Verificar a exibição de mensagem de erro


- Usuário: invalid_user
- Senha: wrong_password


- Mensagem de erro exibida com classe `error-message-container`


- Erro identificado corretamente na interface



---

**Início do teste:** 2025-04-30 10:00  
**Fim do teste:** 2025-04-30 10:01  
**Duração total:** 00:01:00
