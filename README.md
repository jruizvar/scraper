# Execução da API

- Fazer login no [Docker Playground](https://labs.play-with-docker.com/)
- Criar uma instância e dentro dela clonar este repositório: git clone https://github.com/jruizvar/scraper.git
- Entrar no repositório (`cd scraper`) e criar uma imagem executando o comando `docker build --tag scraper:1.0 .`
- Para rodar o container execute o comando `docker run --publish 8080:80 scraper:1.0`

Agora pode abrir o navegador no endereço IP da máquina instanciada no porto 8080. Digite o nome do seu canal de Youtube favorito, e fazer click em download para baixar um arquivo CSV com as descrições dos videos mais populares.
