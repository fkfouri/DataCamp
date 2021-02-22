## Configuração de Ambiente Virtual

1 - Instalando o ambiente virtual Python

`pip install virtualenv`

2 - Criando o ambiente virtual chamando 'env'.

`python -m venv env`

2 - Habilitando o ambiente virtual

`.\env\Scripts\activate`

3 - Atualizar pip
`python -m pip install --upgrade pip`

## Instalando os pacotes a partir do requirement file

`pip install -r requirements.txt`

## Configurando Virtualenv para o Jupyter
https://janakiev.com/blog/jupyter-virtual-envs/

`pip install ipykernel`

`python -m ipykernel install --name=env`

`jupyter notebook`

![alt text](https://miro.medium.com/max/580/1*p2SCVuUuvRoJQS_zgd3Xnw.png)


## Configurando Extensoes para o Jupyter
https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231

`pip install jupyter_contrib_nbextensions`

`jupyter contrib nbextension install`