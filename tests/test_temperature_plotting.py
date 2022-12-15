import pytest, os

import temperature_plotting as tpl

@pytest.mark.skip(reason='Test is bad')
def test_compute_mean1():
    calc = tpl.compute_mean([0,10,20])
    assert calc == 10
    assert type(calc) == float
    

 
def test_compute_mean2():
    
    calc = tpl.compute_mean([-10,10])
    assert calc == 0
    
    calc = tpl.compute_mean([0,10,0])
    assert round(calc,4) == 3.3333, "Check that the average is roughly correct" 
    #when adding a custom comment, pytest will not prnt a message
    
    with pytest.raises(TypeError):
        calc = tpl.compute_mean(['a', 'b', 'c'])
    
    calc = tpl.compute_mean([]) #think about about what the output should be
    assert calc == None
