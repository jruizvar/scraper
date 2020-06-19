# Execução da API

- Fazer login no [Docker PlayGround](https://labs.play-with-docker.com/)
- Criar uma instância e dentro dela clonar este repositório: git clone https://github.com/jruizvar/scraper.git
- Para criar uma imagem execute o comando `docker build --tag scraper:1.0 .`
- Para executar o container execute o comando `docker run --publish 8080:80 scraper:1.0`

Agora pode abrir o navegador no endereço IP da máquina instanciada no porto 8080. Digite o nome do seu canal de Youtube favorito, e fazer click em download para baixar um arquivo CSV com as descrições dos videos mais populares.
