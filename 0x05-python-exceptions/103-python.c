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
	long unsigned int size;
	unsigned int i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	if (!PyList_Check(list))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
		if (!strcmp(type, "float"))
			print_python_float(list->ob_item[i]);
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
