def register_static_metrics():
    pass


class DynamicMetricsCollector:
    def collect(self):
        pass

    # we have to implement a describe method, that returns an empty list, because we can't accept that 'collect' get's
    # called on every server startup (including commands like 'test' or 'migrate'.
    # TODO: maybe its an option do implement a proper describe method, that returns the description of the collector
    def describe(self):
        return []
