# FastApi and Strawberry GraphQl Example

### Pock of a GraphQL Service endpoint built with [FastAPI](https://fastapi.tiangolo.com/) and [Strawberry GraphQL](https://strawberry.rocks/)

![GitHub repo size](https://img.shields.io/github/repo-size/fvitor7/FastApi-and-Graphql-Example?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/FVitor7/FastApi-and-Graphql-Example?style=for-the-badge)

<img src="https://i.imgur.com/rPmZnXI.png" alt="FastAPI and GraphQL screen">

> Preview 
---

## Clone
```bash
git clone https://github.com/FVitor7/FastApi-and-Graphql-Example.git
```

```
pip install -r requirements.txt
```

## 🚀 Run Project


```
uvicorn app.app:app --reload
```
### URL to GraphQl:

```
http://localhost:8000/graphql
````
## Consult Query User and Address

```
query {
  allUsers{
    name
    address {
      cep
    }
  }
  allAddress {
    cep
    user {
      name
    }
  }
}
````

## Create Mutation User and Address Example

```
mutation {
  createUser(
    birthDate: "14/01/1981", 
    cpf: "74319963148", 
    email: "marcosmatheusericksouza_@impactatp.com.br", 
    name: "danielajessicadacunha_@focusnetworks.com.br") {
    name
  }
  createAddress(
    cep: "65082210",
    city: "São Luís", 
    district: "São Raimundo(Anjo da Guarda)", 
    number: "965", 
    street: "Rua Três", 
    userId: 4) {
    id
  }
}

````

## 🤝 Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/FVitor7">
        <img src="https://avatars2.githubusercontent.com/u/48036134?s=460&u=83e0e7eb1fe80c60164e6c9561a6174874c3b3da&v=4" width="100px;" alt="Foto do Fábio Vitor no GitHub"/><br>
        <sub>
          <b>Fábio Vitor</b>
        </sub>
      </a>
    </td>
    
  </tr>
</table>


[⬆ Voltar ao topo](#user-content-fastapi-and-strawberry-graphql-example)<br>
