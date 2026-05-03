from app.k8s_client import get_nodes, get_pods


def test_get_nodes_returns_list():
    result = get_nodes()
    assert isinstance(result, list)


def test_get_pods_returns_list():
    result = get_pods()
    assert isinstance(result, list)