Integração Contínua
===================

A integração contínua (CI) do Space visa automatizar o processo de construção, teste e deploy das aplicações frontend (React) e backend (API Laravel), garantindo a qualidade do código e agilidade na entrega de novas funcionalidades.  Utilizamos o GitHub Actions para orquestrar os pipelines de CI/CD e o Kubernetes para o deploy das aplicações. As imagens Docker são construídas e armazenadas no Docker Hub.  Devido à arquitetura da aplicação, com frontend e backend isolados, mantemos imagens Docker separadas para cada um, além de ambientes de homologação e produção isolados, com seus respectivos bancos de dados.

Fluxo de CI/CD:

O fluxo de CI/CD é dividido em pipelines separados para backend e frontend, e para os ambientes de homologação e produção.  A seguir, detalhamos o processo para o backend, que serve de exemplo para o frontend, com as devidas adaptações:

    Desenvolvimento: Desenvolvedores trabalham em suas branches e realizam commits.

    Homologação: Pushes para a branch homolog disparam o pipeline de CI/CD de homologação do backend.

    Pipeline de Homologação (Backend):
        O GitHub Actions faz o checkout do código.
        Realiza o login no Docker Hub utilizando as credenciais armazenadas nos secrets do GitHub.
        Constrói a imagem Docker do backend utilizando o Dockerfile específico. A imagem é tageada com a versão (ex: artearenahub/space-backend-homolog:0.0.${{github.run_number}}) e também com a tag latest.
        Envia a imagem para o Docker Hub.
        O Kubernetes busca a imagem mais recente do Docker Hub e atualiza o deployment do backend no ambiente de homologação. O arquivo deploy.yml exemplifica a configuração do deployment, incluindo a referência à imagem e os secrets para as variáveis de ambiente.

    Produção: Pull Requests (PRs) para a branch main são utilizados para o deploy em produção. Ao serem fechados, disparam o pipeline de produção.

Padrões Adotados:
=================

    Branching Model: Utilizamos um modelo de branching baseado em Gitflow, com branches homolog e main para os respectivos ambientes.
    Dockerização: Todas as aplicações são dockerizadas, garantindo a portabilidade e consistência entre os ambientes.
    Gerenciamento de Imagens: O Docker Hub é utilizado como repositório centralizado para as imagens Docker.
    Orquestração de Deployments: O Kubernetes gerencia os deployments das aplicações, permitindo o escalonamento e o rolling updates.
    Secrets: As credenciais e informações sensíveis são armazenadas como secrets no GitHub e no Kubernetes, evitando a exposição em código.
    Automatização: Todo o processo de build, teste e deploy é automatizado, reduzindo o tempo de entrega e minimizando erros humanos.
    Ambientes Isolados: Os ambientes de homologação e produção são completamente isolados, incluindo seus respectivos bancos de dados, garantindo que as alterações em homologação não afetem a produção.

Essa abordagem de integração contínua permite que a equipe do Space entregue novas funcionalidades de forma rápida e segura, com alta qualidade e confiabilidade.  A separação entre frontend e backend, e entre ambientes, garante flexibilidade e escalabilidade para o crescimento da aplicação.

Integração Contínua do Backend
===============================

    Pipeline de Produção (Backend):
        O GitHub Actions faz o checkout do código.
        Realiza o login no Docker Hub.
        Constrói a imagem Docker do backend, tageando-a de forma similar ao ambiente de homologação (ex: artearenahub/space-backend:0.0.${{github.run_number}} e artearenahub/space-backend:latest).
        Envia a imagem para o Docker Hub.
        O Kubernetes atualiza o deployment do backend no ambiente de produção, similar ao processo de homologação, porém utilizando os arquivos de configuração específicos para produção.



Integração Contínua do Frontend
===============================

Integração Contínua do Frontend

O processo de integração contínua do frontend do Space segue uma estrutura semelhante à do backend, mas com algumas diferenças importantes devido à natureza da aplicação React.  Assim como o backend, utilizamos GitHub Actions, Docker e Kubernetes para automatizar o processo.

Diferenças entre CI/CD do Frontend e Backend:

    Construção da Aplicação:

    Backend (Laravel): O backend é construído através da execução de comandos como composer install (para dependências PHP) e outros comandos específicos da linguagem e framework. A construção resulta em um conjunto de arquivos que são empacotados na imagem Docker.
    Frontend (React): O frontend React passa por um processo de build utilizando ferramentas como npm build ou yarn build. Esse processo otimiza o código, minifica arquivos JavaScript e CSS, e gera os arquivos estáticos que serão servidos por um servidor web dentro do container Docker.

    Servidor Web:

    Backend: O backend Laravel geralmente é servido por um servidor web como Nginx ou Apache dentro do container Docker.
    Frontend: O frontend React, após o build, consiste em arquivos estáticos. Dentro do container Docker, utilizamos um servidor web como Nginx ou serve para servir esses arquivos estáticos. Isso é uma diferença crucial, pois o frontend não precisa de um framework PHP rodando em produção, apenas um servidor web para entregar os arquivos estáticos.

    Variáveis de Ambiente:

    Backend: As variáveis de ambiente do backend são geralmente gerenciadas através de arquivos .env e secrets do Kubernetes. Essas variáveis são acessadas pela aplicação Laravel durante a execução.
    Frontend: No frontend React, as variáveis de ambiente são frequentemente definidas durante o processo de build e incorporadas aos arquivos estáticos. Utilizamos o mesmo padrão de arquivos .env, com a diferença que, no deploy, usamos o envsubst para substituir as variáveis no arquivo de configuração do Nginx. O exemplo dos arquivos de workflow demonstra a criação do arquivo .env com as variáveis corretas para cada ambiente.

    Deploy no Kubernetes:

    Backend: O deploy do backend no Kubernetes envolve a criação de deployments e services que expõem a API Laravel.
    Frontend: O deploy do frontend também envolve deployments e services, mas o service geralmente expõe a porta do servidor web que serve os arquivos estáticos do React. O arquivo deploy.yml do frontend demonstra a configuração do deployment, incluindo a referência à imagem e a porta 3000, que é a porta padrão do servidor web que serve os arquivos estáticos do React.

    Processo de Deploy:

    Backend: O deploy do backend geralmente envolve a atualização da imagem no Docker Hub e a atualização do deployment no Kubernetes, que automaticamente puxa a nova imagem.
    Frontend: O processo é similar, mas a imagem do frontend contém os arquivos estáticos já construídos.

Detalhes do Workflow do Frontend:

    Homologação: O workflow de homologação do frontend é acionado por pushes para a branch homolog. Ele define as variáveis de ambiente específicas para homologação (ex: NEXT_PUBLIC_API=https://api-homolog.spacearena.net), constrói a imagem Docker com essas variáveis incorporadas, e a envia para o Docker Hub. O Kubernetes então atualiza o deployment com a nova imagem.
    Produção: O workflow de produção é acionado quando um Pull Request para a branch main é fechado (e mergeado). Similarmente ao workflow de homologação, ele define as variáveis de ambiente de produção (ex: NEXT_PUBLIC_API=https://api.spacearena.net), constrói a imagem e a envia para o Docker Hub. O Kubernetes atualiza o deployment de produção.

Padrões Adotados (Frontend):

Além dos padrões já mencionados para o backend (Dockerização, Docker Hub, Kubernetes, Secrets, Automatização, Ambientes Isolados), o frontend também adota:

    Build Otimizado: O processo de build do React garante que os arquivos estáticos sejam otimizados para produção.
    Servidor Web Estático: Um servidor web leve (Nginx ou serve) é utilizado dentro do container Docker para servir os arquivos estáticos do React.

Em resumo, o processo de CI/CD do frontend é adaptado para as características específicas de uma aplicação React, com foco na construção otimizada dos arquivos estáticos, definição de variáveis de ambiente durante o build e utilização de um servidor web para servir esses arquivos.
