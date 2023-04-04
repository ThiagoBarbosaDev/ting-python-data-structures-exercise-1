from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._queue = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if not len(self._queue) < 1:
            return self._queue.pop(0)
        return None

    def search(self, index):
        """Aqui irá sua implementação"""
        try:
            if (
                (index + 1) > len(self._queue)
                or index < 0
                or len(self._queue) == 0
            ):
                print(index + 1, len(self._queue))
                raise IndexError
            return self._queue[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")


# q = Queue()
# queue = Queue()
# print(queue.search(-1))
