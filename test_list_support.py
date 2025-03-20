from holey.core import SymbolicTracer, SymbolicList, make_symbolic

def test_concrete_list():
    tracer = SymbolicTracer()
    lst = SymbolicList([1, 2, 3], tracer=tracer)
    print(f"Concrete list: {lst}")
    assert lst.concrete == [1, 2, 3]
    
def test_symbolic_list():
    tracer = SymbolicTracer()
    lst = SymbolicList(name="sym_list", tracer=tracer)
    print(f"Symbolic list: {lst}")
    assert lst.name == "sym_list"
    assert lst.concrete is None
    
def test_make_symbolic_list():
    tracer = SymbolicTracer()
    lst = make_symbolic(list, "test_list", tracer=tracer)
    print(f"Make symbolic list: {lst}")
    assert lst.name == "test_list"
    
def test_list_equality():
    tracer = SymbolicTracer()
    lst1 = SymbolicList([1, 2, 3], tracer=tracer)
    lst2 = SymbolicList([1, 2, 3], tracer=tracer)
    lst3 = SymbolicList([4, 5, 6], tracer=tracer)
    
    print(f"List equality test: {lst1 == lst2}, {lst1 == lst3}")
    
if __name__ == "__main__":
    test_concrete_list()
    test_symbolic_list()
    test_make_symbolic_list()
    test_list_equality()
    print("All tests passed!")
