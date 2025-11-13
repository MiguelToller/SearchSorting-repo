# 🌳 B-Tree

Uma **B-Tree** (ou Árvore B) é uma estrutura de dados balanceada e autoajustável, muito utilizada em sistemas de gerenciamento de banco de dados e sistemas de arquivos. Ela é projetada para armazenar dados de forma eficiente e facilitar a busca, inserção e exclusão de elementos.

## 🚀 Características principais:

- **Balanceamento**: A B-Tree mantém os dados de forma balanceada, o que significa que todas as folhas estão no mesmo nível. 
- **Ordenação**: Os dados na árvore são armazenados em ordem crescente (ou decrescente), permitindo buscas eficientes. 
- **Nós com múltiplas chaves**: Cada nó pode conter várias chaves e filhos, o que reduz a altura da árvore e melhora a performance de busca.  
- **Eficiência em disco**: É ideal para armazenar grandes volumes de dados que não cabem completamente na memória, pois minimiza o número de acessos ao disco. 

## 🔍 Operações

- **Busca**: A busca é feita de forma eficiente, comparando as chaves dentro dos nós até encontrar a chave desejada ou identificar que ela não existe. 
- **Inserção**: Ao inserir uma chave, a árvore pode dividir seus nós para garantir que ela continue balanceada. 
- **Exclusão**: Similar à inserção, a exclusão pode envolver a fusão de nós para manter a estrutura balanceada. 

## 🌱 Estrutura

- **Raiz**: O nó superior da árvore. 
- **Nós internos**: Contêm chaves e ponteiros para outros nós. 
- **Folhas**: Contêm as chaves finais e não possuem filhos. 

## 💡 Vantagens

- A B-Tree é ideal para operações que exigem acesso a grandes volumes de dados, como índices de banco de dados, pois reduz a complexidade de buscas, inserções e exclusões em grandes quantidades de dados. 
- Sua estrutura balanceada garante que todas as operações tenham um tempo de execução eficiente, com complexidade **O(log n)**. 

## 📊 B-Tree Visualization

![Exemplo Visual da B-Tree](https://github.com/MiguelToller/SearchSorting-repo/blob/main/B-Tree/B-Tree%20Visual.png)
