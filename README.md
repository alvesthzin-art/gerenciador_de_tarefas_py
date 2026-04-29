# 📝 Gerenciador de tarefas

Um gerenciador de listas de tarefas (To-Do List) desenvolvido em Python, focado em execução via terminal. O projeto foi criado para demonstrar conceitos fundamentais de manipulação de dados e persistência de arquivos.

## 🎯 Objetivo do Projeto
Este software serve para organizar a rotina diária do usuário, permitindo o registro, visualização e conclusão de atividades. O diferencial é a **persistência de dados**: ao contrário de scripts simples, as informações aqui não são perdidas ao fechar o programa, pois são ancoradas em um banco de dados local.

## 🚀 Funcionalidades
- **Adicionar Tarefas:** Registro rápido de novas atividades com status inicial pendente.
- **Listagem Dinâmica:** Exibição organizada com marcadores visuais (`[ ]` para pendentes e `[✔]` para concluídas).
- **Conclusão de Atividades:** Interface interativa para marcar tarefas como feitas através de índices numéricos.
- **Persistência de Dados (Auto-Save):** Salvamento automático em arquivo JSON para que os dados sobrevivam ao fechamento do aplicativo.

## 📂 Como os dados são armazenados?
O projeto utiliza o formato **JSON (JavaScript Object Notation)** para o armazenamento. 
- Quando você fecha o programa, o Python converte a lista de tarefas em um texto estruturado e o grava no arquivo `tarefas.json`.
- Ao iniciar, o programa lê esse arquivo e reconstrói a lista exatamente como você a deixou.



## 🛠️ Tecnologias e Conceitos Aplicados
- **Python 3.x:** Linguagem base do projeto.
- **Manipulação de Arquivos (I/O):** Leitura e escrita de arquivos locais utilizando a biblioteca `os`.
- **Serialização de Dados:** Uso da biblioteca `json` para converter objetos Python em um formato de armazenamento universal.
- **Tratamento de Exceções:** Implementação de blocos `try/except` para garantir que o programa não trave caso o usuário digite comandos inválidos.

--------------------

👨‍💻 Desenvolvedor
<table style="border: none;">
<tr>
<td align="center">
<a href="#">
<img src="https://github.com/alvesthzin-art.png" width="100px;" alt="Avatar"/><br />
<sub><b>@alvesthzin-art</b></sub>
</a>
</td>
