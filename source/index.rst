.. Space Arena documentation master file, created by
   sphinx-quickstart on Mon Nov 25 11:07:32 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bem vindo à Documentação do Space!
===================================

**Space** (/speɪs/) é um ERP para gestão da empresa Arte Arena. 
Usando principalmente as linguagens PHP e Typescript, Space é um software 
de gestão empresarial  que ajuda as empresas Arte Arena a gerenciar seus 
produtos, pedidos, vendas, clientes, fornecedores, produção, contas etc.

.. image:: _static/images/dark-logo.svg

Space oferece uma API intuitiva e um conjunto de funcionalidades prontas para 
uso por todos os setores da empresa, oferecendo uma especial interface para 
acompanhamento dos pedidos, desde a venda até a entrega, passando pela 
arte-final, bem como pela impressão, confecção e demais etapas produtivas.

A interface visual do Space faz uso do Next.js, parte do template Modernize,
e oferece o acesso para os usuários logados conforme seus perfis de acesso.

.. note::

   A arquitetura básica do backend é uma API feita em Laravel (PHP), enquanto o 
   frontend resume-se a uma aplicação React a partir do Next.js (Typescript).


.. toctree::
   :maxdepth: 2
   :caption: Conteúdos:

   introducao/introducao
   arquitetura/arquitetura
   metodologia/metodologia
   guia_de_uso
   faq
   releases
   
...
Para mais informações, consulte a sessão :ref:`guia_de_uso`.
