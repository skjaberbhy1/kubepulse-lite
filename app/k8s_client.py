from kubernetes import client, config

try:
    config.load_incluster_config()
except:
    config.load_kube_config()

v1 = client.CoreV1Api()

def get_nodes():
    nodes = v1.list_node()

    result = []

    for node in nodes.items:
        result.append({
            "name": node.metadata.name,
            "labels": node.metadata.labels,
            "creation_time": str(node.metadata.creation_timestamp)
        })

    return result

def get_pods():
    pods = v1.list_pod_for_all_namespaces()

    result = []

    for pod in pods.items:
        result.append({
            "name": pod.metadata.name,
            "namespace": pod.metadata.namespace,
            "status": pod.status.phase,
            "node": pod.spec.node_name
        })

    return result
