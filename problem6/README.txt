ATENÇÃO: Os programas foram desenvolvidos em python versão = 3.4.1 no S.O Windows 7


Executar programa de geração de amostras: “samples_generator.py” que recebe os parâmetros: 
-s = sample-number, quantidade de amostras a serem geradas. Valor padrão = 100
-t = threshold, valor de θ; valor padrão = 5.0
-i = ini, valor inicial do domínio da função. Valor padrão = 0.0
-e = end, valor final do domínio da função. Valor padrão = 10.0
-o = output file, arquivo de amostras no formato json, Valor padrão ./samples.json

A executar o gerador de amostras serão gerados amostras em json com o seguinte formato:
[[valor gerado, {1 ou 0}], [valor gerado, {1 ou 0}], [valor gerado, {1 ou 0}]] 

Então executar o programa “main .py” que gera o classificador apartir do algoritmo de perceptron, esse programa recebe o seguinte parâmetro:
-t = training_data_file, arquivo json geradpo pelo programa samples_generator. Valor padrão = “./samples.json”

Então entre com os valores de x, e o programa retorna o y de acordo com o conceito aprendido.

O algoritmo do perceptron está no arquivo “Perceptron.py”

O arquivo exec.bat é um exemplo de execução para teta=5.0 que pode rodar em sistemas windows e pode ser facilmente adaptado para rodar
em sistemas linux também.