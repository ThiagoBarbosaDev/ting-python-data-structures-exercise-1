from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    queue = PriorityQueue()
    queue.enqueue({"qtd_linhas": 3})
    queue.enqueue({"qtd_linhas": 5})
    queue.enqueue({"qtd_linhas": 10})
    queue.enqueue({"qtd_linhas": 4})
    queue.enqueue({"qtd_linhas": 7})
    assert queue.dequeue() == {"qtd_linhas": 3}
    assert len(queue) == 4
    assert queue.search(0) == {"qtd_linhas": 4}
    assert queue.search(1) == {"qtd_linhas": 5}
    assert queue.search(2) == {"qtd_linhas": 10}
    assert queue.search(3) == {"qtd_linhas": 7}
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(99)
