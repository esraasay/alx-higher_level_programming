#include <python.h>
/**
 * print_python_list_info - print basic information about python list.
 * @p: pyobject list
 */
void print_python_list_info(pyobject *p)
{
	int size, alloc, i;
	pyobject *obj;

	size = py_size(p);
	alloc = ((pylistobject *)p)->alloc;
	printf("[*] size of the python list = %d\n", size);
	printf("[*] alloc = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		printf("element %d\n", i);
		obj = pylist_Getitem(p, i);
		printf("%s\n", py_type(obj)->tp_name);
	}
}
