from ting_file_management.file_management import txt_importer
import sys


def is_repeated(path_file, instance):
    """checks the queue if the file is already inserted"""
    for index in range(0, len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return True

    return False


def create_data(path_file, text):
    """creates the data in dictionary structure"""
    data = dict()
    data["nome_do_arquivo"] = path_file
    data["qtd_linhas"] = len(text)
    data["linhas_do_arquivo"] = text

    return data


def process(path_file, instance):
    """Aqui irá sua implementação"""
    if is_repeated(path_file, instance):
        return

    text = txt_importer(path_file)
    data = create_data(path_file, text)

    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    is_queue_empty = len(instance) == 0

    if is_queue_empty:
        return print('Não há elementos')

    file = instance.dequeue()["nome_do_arquivo"]
    print(f"Arquivo {file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        print(instance.search(position))
    except IndexError:
        print('Posição inválida', file=sys.stderr)
