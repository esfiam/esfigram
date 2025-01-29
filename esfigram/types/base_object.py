class BaseObject:
    """
    A base class to manage hierarchical data structures with dynamic attribute assignment
    and serialization to dictionaries.
    """
    def __init__(self, **kwargs):
        def _to_base_object(item):
            if isinstance(item, dict):
                return BaseObject(**item)
            elif isinstance(item, list):
                return [_to_base_object(i) for i in item]
            return item

        for key, value in kwargs.items():
            setattr(self, key, _to_base_object(value))

    def to_dict(self) -> dict:
        """
        Recursively converts the object and its attributes into a dictionary.
        """
        def _to_dict(item):
            if isinstance(item, BaseObject):
                return item.to_dict()
            elif isinstance(item, list):
                return [_to_dict(i) for i in item]
            return item

        return {key: _to_dict(value) for key, value in self.__dict__.items()}

    def __repr__(self) -> str:
        """
        Provides a string representation of the object for debugging.
        """
        return f"{self.__class__.__name__}({self.to_dict()})"