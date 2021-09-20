import pandas as pd

df = pd.read_csv("data_set/nomes_pre_tratados_famosos.csv")
lista_presidentes = [
    "josé sarney",
    "sarney",
    "fernando collor",
    "collor",
    "itamar franco",
    "fernando henrique cardoso",
    "luiz inácio lula da silva",
    "lula",
    "lulinha",
    "dilma rouseff",
    "dilmão",
    "dilmãe",
    "michel temer",
    "vampiro",
    "jair jolsonaro",
    "birolibo",
    "bozo",
    "birobiro",
    "bozonaro",
    "bolsonaro",
]


def get_lista_nomes():
    names = [x for x in df["names"]]
    nomes_tratados = []
    for x in names:
        for y in x.split("|"):
            nomes_tratados.append(y)
    value = [z for z in nomes_tratados if z != '']
    value = value + lista_presidentes
    string_list = [each_string.lower() for each_string in value]
    return string_list
