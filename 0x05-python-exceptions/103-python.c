#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

/**
 * print_python_list - A funnction that prints information about a Python list
 * @p: A pointer to the Python list object
 * This program conforms to the betty documentation style
 **/

void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *element;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: ", i);

		if (PyBytes_Check(element))
			printf("bytes\n"), print_python_bytes(element);
		else if (PyFloat_Check(element))
			printf("float\n"), print_python_float(element);
		else if (PyLong_Check(element))
			printf("int\n");
		else if (PyUnicode_Check(element))
			printf("str\n");
		else if (PyList_Check(element) || PyTuple_Check(element))
			printf("list\n"), print_python_list(element);
		else
			printf("unknown\n");
	}
}

/**
 * print_python_bytes - A function that prints information about a Python
 * bytes object
 * @p: A pointer to the Python bytes object
 * This program conforms to the betty documentation style
 **/

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes_str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes_str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_str);

	printf("  first %d bytes: ", (int)(size > 10 ? 10 : size));
	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf("%02x ", (unsigned char)bytes_str[i]);
	}
	printf("\n");
}

/**
 * print_python_float - A function that prints information about
 * a Python float object
 * @p: A pointer to the Python float object
 * This program conforms to the betty documentation style
 **/

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AsDouble(p));
}
