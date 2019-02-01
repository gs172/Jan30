import pytest
@pytest.mark.parametrize("a,b,c,d,e",[
										(5,3,2,5,2),
										(5,-2,7,7,-2),
										(30,20,10,30,10),
										])
def test_list(a,b,c,d,e):
	from find import find_ex_list
	
	answer = find_ex_list(a,b,c)
	assert answer ==d

@pytest.mark.parametrize("a,b,c,d,e",[
										(5,3,2,5,2),
										(5,-2,7,7,-2),
										(30,20,10,30,10),
										])
def test_list1(a,b,c,d,e):
	from find import find_ex_list1
	
	answer1 = find_ex_list1(a,b,c)
	assert answer1 ==e

@pytest.mark.parametrize("a,b,c,d,e",[
										(5,3,2,5,2),
										(5,-2,7,7,-2),
										(30,20,10,30,20),
										])
def test_list2(a,b,c,d,e):
	from find import find_ex_list1
	
	answer2 = find_ex_list1(a,b,c)
	assert answer2 ==e