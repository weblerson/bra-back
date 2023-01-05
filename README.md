# BRA Back
### Backend das aplicações desktop e mobile do projeto de BRA Premens, uma prensa eletromecânica semi-automática monitorada em tempo real.

O projeto BRA Back, atualmente, conta com uma API para a aplicação desktop voltada para empresas, que conta com endpoints para cadastro de novos clientes, alteração de CEP e resgate de clientes cadastrados.

[Clique aqui](https://github.com/weblerson/bra-desktop) para acessar o repositório da aplicação desktop, que está em processo de desenvolvimento.

## Tecnologias Utilizadas:
- Python
- Django
- Django Ninja
- Redis
- MySQL
- Postgres
- Celery
- Docker
- Git

## Como Usar a API:

Por se tratar de uma API de uso exclusivo da aplicação desktop, foi decidido que seria feita a troca de informações por um token JWT, carregando as informações principais.

### Cadastro de Novos Clientes:
##### Endpoint: /api/v1/users
##### Método: POST
##### Body: Token JWT

Para realizar o cadastro de um cliente, é necessário enviar no corpo da requisição um token JWT contendo o nome completo do cliente, o CPF, CEP, e-mail e o cargo.

```json
{
    "token": "token_jwt"
}
```

Como a  aplicação desktop está sendo desenvolvida com Java 17, então temos como exemplo de uma requisição o seguinte método:

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class PremensHttpRequest {

    public static void createUser(String token) {
        HttpClient client = HttpClient.newHttpClient().build();
        URI uri = URI.create("https://www.example.com/api/v1/users");

        HttpRequest request = HttpRequest.newBuilder()
            .POST(BodyPublishers.ofString(String.format("{\"token\": \"%s\"}", token)))
            .uri(uri)
            .headers("Accept", "application/json", "Content-Type", "application/json")
            .build();

        HttpResponse response = httpClient.send(request, BodyHandlers.ofString());

        System.out.println(response.body());
    }
}
```

Dessa forma, é esperado como resposta o seguinte JSON caso tudo ocorra normalmente:

```json
{
    "success": true,
    "body": "Usuário cadastrado com sucesso."
}
```

Mas, caso aconteça algum erro, a resposta esperada é essa:

```json
{
    "success": false,
    "body": "mensagem_de_erro"
}
```

Caso tenha mais de um erro, teremos como resposta na chave "body" um map com a chave sendo o campo onde ocorreu o erro e o valor sendo uma lista com os erros relacionados àquele campo. Por exemplo:

```json
{
    "success": false,
    "body": {
        "cpf": ["O CPF não pode conter menos de 11 dígitos."],
        "cep": ["O CEP não pode conter menos de 8 dígitos."]
    }
}
```

Caso tudo ocorra bem e a requisição tenha sucesso, você vai receber um link no e-mail informado para confirmar sua conta. Clicando no link, vai ser redirecionado para uma página para criar sua senha e, após criar a senha, sua conta será confirmada.

![Página de criação de senha](./src/create_password.png)

![Página de confirmação de conta](./src/account_confirmed.png)