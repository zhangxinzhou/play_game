import ray


@ray.remote
class Counter:
    def __init__(self):
        self.count = 0

    def inc(self, n):
        self.count += n

    def get(self):
        return self.count


# on the driver
counter = Counter.options(name="global_counter").remote()
# get the latest count
print(ray.get(counter.get.remote()))

# in your envs
counter = ray.get_actor("global_counter")
# async call to increment the global count
counter.inc.remote(1)
print(ray.get(counter.get.remote()))