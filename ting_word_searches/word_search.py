def create_match_list(linhas_do_arquivo, target_word):
    match_list = list()
    for index, linha in enumerate(linhas_do_arquivo):
        lower_linha = linha.lower()
        if target_word.lower() in lower_linha:
            match = dict()
            match["linha"] = index + 1
            match_list.append(match)
    return match_list


def create_data(text_data, word):
    """creates the data in dictionary structure"""
    nome_do_arquivo = text_data['nome_do_arquivo']
    linhas_do_arquivo = text_data["linhas_do_arquivo"]
    match_list = create_match_list(linhas_do_arquivo, word)
    print(match_list)
    data = dict()
    data["palavra"] = word
    data["arquivo"] = nome_do_arquivo
    data["ocorrencias"] = match_list

    return data


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    dataset = list()
    for index in range(0, len(instance)):
        text_data = instance.search(index)
        data = create_data(text_data, word)
        are_there_matches = len(data["ocorrencias"])
        if are_there_matches:
            dataset.append(data)
    return dataset


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
