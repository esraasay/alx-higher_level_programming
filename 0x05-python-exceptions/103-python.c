#include <Python.h>
#include <floatobject.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;
	char *data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("size: %zd\n", size);
	printf("trying string: %s\n", data ? data : "(error)");

	printf("first 10 bytes: ");
	for (i = 0; i < size && i < 10; ++i)
	{
		printf("%02x", data[i] & 0xFF);
		if (i < 9)
			printf(" ");
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AS_DOUBLE(p);

	printf("[.] float object info\n");

	if (PyFloat_IS_INTEGER(p))
	{
		printf("value: %0.1f\n", value);
	}
	else
	{
		printf("value: %0.16g\n", value);
	}
}
