ATENÇÃO: Os programas foram desenvolvidos em python versão = 3.4.1 no S.O Windows 7

Executar programa de geração de amostras: “samples_generator.py” que recebe os parâmetros: 
-b = bound, limitante superior ou inferior, pode receber os valores “upper” ou “lower”, sem valor padrão;
-s = sample-number, quantidade de amostras a serem geradas. Valor padrão = 100
-t = threshold, valor de θ; valor padrão = 5.0
-i = ini, valor inicial do domínio da função. Valor padrão = 0.0
-e = end, valor final do domínio da função. Valor padrão = 10.0
-o = output file, arquivo de amostras no formato json, Valor padrão ./samples.json

A executar o gerador de amostras serão gerados amostras em json com o seguinte formato:
[[valor gerado, {1 ou 0}], [valor gerado, {1 ou 0}], [valor gerado, {1 ou 0}]] 

Para a solução do exercício, será necessário executar duas vezes o “sample_generator.py”, um para o limitante inferior “lower” e outro para o superior “upper”,  grave os arquivos json gerados com nomes diferentes e execute o “main.py”

Então executar o programa “main .py” que gera o classificador apartir do algoritmo de perceptron, esse programa recebe os seguinte parâmetro:
-l = lower_tranning_data_file, arquivo json gerado pelo programa samples_generator para limitante inferior. Valor padrão = “./lower_samples.json”
-u = upper_bound_tranning_data_file, arquivo json gerado pelo programa samples_generator para limitante superior. Valor padrão = “./upper_samples.json”
 
O algoritmo do perceptron está no arquivo “Perceptron.py”, nesse o algoritmo gerara dois perceptron e juntara os dois para classificar a entrada pelo console.

O arquivo exec.bat é um exemplo de execução para teta-1=3.0 e teta-2=5.0 que pode rodar em sistemas windows e pode ser facilmente adaptado para rodar
em sistemas linux também.