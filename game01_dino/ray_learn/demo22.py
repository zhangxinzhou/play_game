import ray


@ray.remote
def remote_chain_function(value):
    return value + 1


t1_id = remote_chain_function.remote(value=222)
ray.get(t1_id)
print(ray.get(t1_id))
