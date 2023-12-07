#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints basic information about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, alloc, i;
	PyObject *item;

	printf("[*] Python list info\n");
	size = Py_SIZE(list);
	alloc = list->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; ++i)
	{
		item = list->ob_item[i];
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints basic information about Python bytes objects
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = Py_SIZE(bytes);
	printf("  Size: %ld\n", size);
	printf("  trying string: %s\n", PyUnicode_AsUTF8(PyObject_Repr(p)));
	size = size > 10 ? 10 : size;
	str = (char *)PyBytes_AsString(p);

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; ++i)
		printf("%02hhx%c", str[i], i == size - 1 ? '\n' : ' ');
}
