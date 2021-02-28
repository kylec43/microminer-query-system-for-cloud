from Circular_Shift_Filter import Circular_Shift_Filter
from Alphabetizer_Filter import Alphabetizer_Filter

def Execute_Circular_Shift_Filter(lines):

	circular_shift_filter = Circular_Shift_Filter(lines)
	return circular_shift_filter.Get_Circular_Shifts()



def Excecute_Alphabetizer(lines):
	alphabetizer = Alphabetizer_Filter(lines)
	return alphabetizer.Get_Sorted_Lines()


